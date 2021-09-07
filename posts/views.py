from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, "posts/blog.html",{"posts":posts})


def category(request, category_id):
    category = get_object_or_404(Category,id=category_id)
    posts= category.get_posts.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, "posts/category.html",{"posts":posts, 'category': category})
