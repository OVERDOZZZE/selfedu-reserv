from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from .forms import AddPostFrom
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy
# Create your views here.

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью ', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
]


class GunsHome(ListView):
    model = Guns
    template_name = 'main_app/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Guns.objects.filter(is_published = True)



# def index(request):
#     posts = Guns.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Main Page',
#         'cat_selected': 0
#     }
#     return render(request, 'main_app/index.html', context=context)


def show_category(request, cat_slug):
    posts = Guns.objects.filter(cat__slug=cat_slug)

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Categories',
        'cat_selected': cat_slug
    }
    return render(request, 'main_app/index.html', context=context)


def about(request):
    return render(request, 'main_app/about.html')


class AddPage(CreateView):
    form_class = AddPostFrom
    template_name = 'main_app/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostFrom()
#
#     return render(request, 'main_app/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавить статью'})


def contact(request):
    return render(request, 'main_app/contacts.html')


def login(request):
    return render(request, 'main_app/login.html')


def show_post(request, post_slug):
    post = get_object_or_404(Guns, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }

    return render(request, 'main_app/show_post.html', context=context)


def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
