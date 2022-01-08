from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from courses.models import Category, Courses
from cart.cart import Cart
from cart.forms import CartAddProductForm
from products.models import Product
from forum.models import About, ContactUs


def home(request):
    cart = Cart(request)
    categories = Category.objects.all()
    courses = Courses.objects.all().order_by('-id')[:2]
    total_data = Courses.objects.count()

    # for products
    products = Product.objects.all().order_by('-id')[:2]
    total_products = Product.objects.count()

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    context = {
        'categories': categories,
        'courses': courses,
        'total_data': total_data,
        'products': products,
        'total_products': total_products,
        'cart': cart
    }
    return render(request, 'jtalks/home.html', context)


def load_more_data(request):
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])
    data = Courses.objects.order_by('-id')[offset:offset+limit]
    t = render_to_string('jtalks/more_courses.html', {'data': data})
    return JsonResponse({'data': t})


def load_more_products(request):
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])
    data = Product.objects.order_by('-id')[offset:offset+limit]
    t = render_to_string('jtalks/more_products.html', {'data': data})
    print(data)
    return JsonResponse({'data': t})


def search_more_products(request):
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])
    search = request.GET['search']
    search_data = Q(name__icontains=search)
    data = Product.objects.filter(search_data).order_by('id')[offset:offset+limit]
    t = render_to_string('jtalks/search_products.html', {'data': data})
    return JsonResponse({'data': t})

"""
def home(request):
    categories = Category.objects.all()
    courses_list = Courses.objects.all()
    paginator = Paginator(courses_list, 3)
    page = request.GET.get('page')
    courses = paginator.get_page(page)
    context = {
        'categories': categories,
        'courses': courses
    }
    return render(request, 'jtalks/home.html', context)
"""

# AboutUs Views
def about(request):
    about = About.objects.all()
    context = {
    'abouts': about,    
    }
    return render(request, 'jtalks/about.html', context)

# ContactUs Views
def contact_us(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        subject = request.POST['subject']
        message = request.POST['message']

        ContactUs.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            address=address,
            subject=subject,
            message=message
        )
        return render(request, 'jtalks/contact_us_success.html')
    return render(request, 'jtalks/contact.html')


class GetCourses(View):
    def get(self, request):
        get_courses = Courses.objects.filter(available=True)
        courses = []
        data = {}
        for i in range(len(get_courses)):
            x = get_courses[i].created
            datex = x.strftime("%d-%m-%Y")
            timex = x.strftime("%I:%M:%S %p")
            date_sent = datex + ' ' + 'at' + ' ' + timex
            cors = {
                'id': get_courses[i].id,
                #'categories': get_courses[i].categories.courses.all,
                'name': get_courses[i].name,
                'overview': get_courses[i].overview,
                'cover': get_courses[i].cover.url,
                'slug': get_courses[i].slug,
                'content_url': get_courses[i].content_url,
                'content_file': get_courses[i].content_file.url,
                'tutor': get_courses[i].tutor,
                'tutor_image': get_courses[i].tutor_image.url,
                'tutor_title': get_courses[i].tutor_title,
                'price': get_courses[i].price,
                'created': date_sent,
                'updated': get_courses[i].updated,
            }
            courses.append(cors)
        data['courses'] = courses
        return JsonResponse(data)


def search_products(request):
    query_product = request.POST.get('product')
    search_data = Q(name__icontains=query_product)
    search_results = Product.objects.filter(search_data).distinct()
    print(search_results)
    total_products = search_results.count()
    context = {
        'search_results': search_results,
        'query_product': query_product,
        'total_products': total_products
    }
    return render(request, 'jtalks/product_search.html', context)