from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Category, Comment
from .forms import CategoryForm, CommentForm


def post_list(request):
    all_posts = Post.objects.all().order_by('-date')
    paginator = Paginator(all_posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    categories = Category.objects.all()

    if request.method == 'POST':
        query = request.POST.get('q', None)
        submit_button = request.POST.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query) | Q(body__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            context = {
                'query': query,
                'results': results,
                'submit_button': submit_button
            }
            return render(request, 'forum/search_results.html', context)
    context = {
        'posts': posts,
        'categories': categories,
        'title': all_posts[0].title if all_posts else None,
        'id': all_posts[0].id if all_posts else None,
        'slug': all_posts[0].slug if all_posts else None,
    }
    return render(request, 'forum/post_list.html', context)


def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    comments = post.comments.filter(active=True).order_by('-updated')
    new_comment = None
    liked = False
    if post.likes.filter(id=request.user.id).exists:
        liked = True
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'liked': liked
    }
    return render(request, 'forum/post_detail.html', context)


@login_required
def post_create(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        user_category = request.POST['category']
        title = request.POST['title']
        body = request.POST['body']
        image = request.FILES['photo']

        t_str = title.lower()
        for i in range(0, len(t_str), 1):
            if t_str[i] == ' ':
                t_str = t_str.replace(t_str[i], '-')

        category = Category.objects.get(name=user_category)

        new_post = Post.objects.create(author=request.user, slug=t_str, title=title, body=body, image=image)
        new_post.save()
        new_post.categories.add(category)
        return redirect('/forum/')

    context = {
        'categories': categories
    }
    return render(request, 'forum/post_new.html', context)


@login_required
def post_edit(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)

    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        post.title = title
        post.body = body
        post.save()
        return redirect('/forum/')

    context = {
        'post': post
    }
    return render(request, 'forum/post_edit.html', context)


@login_required
def post_delete(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    if request.method == 'POST':
        ask = request.POST['ask']
        if ask == 'Yes':
            post.delete()
            return redirect('/forum/')
        elif ask == 'No':
            return redirect('/forum/')
    return render(request, 'forum/post_delete.html', {'post': post})


def like_view(request, id, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id'), slug=slug)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('forum:post_detail', args=[int(id), str(slug)]))


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            categories = Category.objects.all()
            context = {
                'categories': categories
            }
            return render(request, 'forum/post_new.html', context)

    else:
        form = CategoryForm()
    return render(request, 'forum/category.html', {'form': form})


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-date'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "forum/category_post_list.html", context)
