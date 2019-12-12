from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
     path('register/', views.RegisterFormView.as_view(), name='register'),
     path('login/', views.LoginFormView.as_view(), name='login'),
     path('logout/', views.LogoutView.as_view(), name='logout'),
     path('', views.product_list, name='product_list'),
     path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
     path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]
