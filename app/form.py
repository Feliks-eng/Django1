from django import forms
from app.models import Product
from django.contrib.auth.models import User

# Форма Регистрации с добавленным значением в виде виджета который способен(скрывать вписываемые символы а также указывает браузеру что поле предназначена для пароля)
class UserRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']




# Форма товаров
class ProductInfo(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'