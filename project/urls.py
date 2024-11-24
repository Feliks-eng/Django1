from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    # Админ панель (админка)
    path('admin/', admin.site.urls),
    # Url главной страницы(home.html)
    path('', views.home, name='home'),
    # Url регистрации
    path('register/', views.register, name='register'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # Url корзины
    path('card/', views.view_cart, name='view_cart'),
    # Вспомогающий Url для монипуляций такая как удалени товара из корзины
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]

