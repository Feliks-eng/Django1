from django.shortcuts import render, redirect, get_object_or_404
from app.models import Product,Cart
from app.form import UserRegister
from django.contrib.auth import login , authenticate
from django.contrib import messages

# Главная страница сайта 
def home(request):
    return render(request, 'home.html')


# Форма главной страницы
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            messages.success(request , "Вы успешно зарегестрировались!") # Месседж после успешной регистрации
            # Перенаправляет на главную страницу сайта
            return redirect('home')  
    else:
        form = UserRegister()

    return render(request, 'register.html', {'form': form})




# Форма корзины
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)

# Добовляет обьект по одному а после сохраняет его
    if not created:
        cart_item.quantity += 1
        cart_item.save()
# В случае которого переносит на url самой корзины
    return redirect('view_cart')

def view_cart(request):
    cart_items = Cart.objects.all()
    # Добавляем атрибут total_price для каждого элемента корзины
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'card.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, cart_item_id):
    # Получаем объект товара в корзине
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    # Удаляет товар из корзины 
    cart_item.delete()
    # Перенаправляем обратно в корзину
    return redirect('view_cart')