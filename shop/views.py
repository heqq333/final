from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from kart.form import CartAddProductForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

def product_list(request, category_slug=None):
     category = None
     categories = Category.objects.all()
     products = Product.objects.filter(available=True)
     if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
     products = products.filter(category=category)
     return render(request, 'shop/product/list.html',
         {'category': category,
         'categories': categories,
         'products': products})

def product_detail(request, id, slug):
     product = get_object_or_404(Product, id=id, slug=slug, available=True)
     cart_product_form = CartAddProductForm()
     return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "shop/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "shop/login.html"


    success_url = "/"

    def form_valid(self, form):

        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")