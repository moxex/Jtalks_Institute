from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View
from cart.cart import Cart
from cart.forms import CartAddProductForm
from .forms import OrderCreateForm
from .models import Product, OrderItem, Order
from .render import Render


def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'products/details.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'cart': cart
    })


# create orders
def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # clear the cart
            # cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            context = {
                'order': order,
                'cart': cart,
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone_number']
            }
            return render(request, 'products/pay_with_paystack.html', context)
    else:
        form = OrderCreateForm()
        return render(request, 'products/create_order.html', {'cart': cart, 'form': form})


def ajax_payment(request):
    # order_req = get_object_or_404(Order, order_id)
    if request.is_ajax():
        reference_id = request.POST.get('reference')
        x = Order(reference=reference_id, paid=True)
        x.save()
        if x:
            response = {
                'message': "Your Payment was successfully received"
            }
            return JsonResponse(response)
        else:
            response = {
                'message': "Your Payment Failed"
            }
            return JsonResponse(response)


# view for pdf rendering
class Pdf(View):

    def get(self, request, id):
        cart = Cart(request)
        order_item = get_object_or_404(Order, id=id)
        today = timezone.now()
        # clear the cart
        cart.clear()
        params = {
            'id': id,
            'today': today,
            'cart': cart,
            'order_item': order_item,
            # 'request': request
        }
        return Render.render('products/pdf.html', params)
