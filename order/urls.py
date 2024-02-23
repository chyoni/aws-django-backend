from django.urls import path, include
from order import views

app_name = 'orders'
urlpatterns = [
    path('shops/', views.shops, name='shops'),
    path('shops/<int:shop_id>/menus', views.menus, name='menus'),
    path('', views.order, name='order')
]

