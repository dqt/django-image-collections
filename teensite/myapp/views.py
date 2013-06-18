from django.shortcuts import render, render_to_response, get_object_or_404
from teensite.myapp.models import Category, Blog, Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random



def home(request):
    return render(request, 'home.html', {'cats': Category.objects.all(),
                                            'blogs' : Blog.objects.all().order_by("-posted"),
                                            })



def view_categories(request):
    return render_to_response('view_categories.html', {
        'categories': Category.objects.all()
    })

def view_posts(request):
    return render_to_response('view_posts.html', {
        'posts': Blog.objects.all(),
    })



#def view_post(request, slug):
#    return render_to_response('view_post.html', {
#        'cats': Category.objects.all(),
#        'post': get_object_or_404(Blog, slug=slug)
#    })

def view_post(request, slug):
    random_idx = random.randint(0, Blog.objects.count() - 1)
    random_obj = Blog.objects.all()[random_idx]
    twelve = Blog.objects.all()[:12]
    dablog = Blog.objects.get(slug=slug)
    image_list = dablog.images.all()
    paginator = Paginator(image_list, 1)

    page = request.GET.get('page')
    try:
        image = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        image = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        image = paginator.page(paginator.num_pages)

    return render_to_response('view_post.html', {
        'cats': Category.objects.all(),
        "image": image,
        'post': get_object_or_404(Blog, slug=slug),
        'random_obj': random_obj,
        'twelve': twelve,
    })

def view_category(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'cats': categories,
        'category': category,
        'row1' : reversed(Blog.objects.filter(category=category)[:3]),
        'row2' : reversed(Blog.objects.filter(category=category)[3:6]),
        'row3' : reversed(Blog.objects.filter(category=category)[6:9]),
        'row4' : reversed(Blog.objects.filter(category=category)[9:12]),
    })