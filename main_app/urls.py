from django.urls import path
from . import views
from .views import GunsHome, AddPage

urlpatterns = [
    path('', GunsHome.as_view(), name='home'),
    # path('cats/<int:cat_id>/', views.cats, name='cats'),
    path('about/', views.about, name='about', ),
    path('addpage/', AddPage.as_view(), name='add_page', ),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='show_post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category')
]
