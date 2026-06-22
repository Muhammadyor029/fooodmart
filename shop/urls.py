
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('shop/', views.shop_view, name='shop'),
    path('product/<int:id>/', views.single_product_view, name='single_product'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:id>/', views.add_to_cart_view, name='add_to_cart'),
    path('cart/remove/<int:id>/', views.remove_from_cart_view, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('add-blog/', views.add_blog_view, name='add_blog'), 
    path('blogs/', views.blog_list_view, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail_view, name='blog_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile_view, name='profile'),
]