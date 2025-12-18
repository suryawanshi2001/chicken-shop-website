from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('order/<int:pk>/', views.order_page, name='order_page'),
    path('success/', views.success, name='success'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('products/', views.product_list),
    path('order/<int:product_id>/', views.place_order),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('order/delete/<int:order_id>/', views.delete_order),


    # path('products/', product_list, name='products'),
    # path('order/<int:product_id>/', place_order, name='place_order'),
    # #path('my-orders/', my_orders, name='my_orders'),


]
