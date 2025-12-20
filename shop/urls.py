from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),

    # Products
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # Orders (customer)
    path('order/<int:pk>/', views.order_page, name='order_page'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('order/delete/<int:order_id>/', views.delete_order, name='delete_order'),

    # Admin dashboard (custom)
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update-order/<int:order_id>/', views.update_order_status, name='update_order_status'),

    path('success/', views.success, name='success'),
]
