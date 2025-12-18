from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Profile
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import HomeBanner

# Create your views here.


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def order_page(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        qty = int(request.POST['quantity'])
        address = request.POST['address']
        total = product.price * qty

        Order.objects.create(
            product=product,
            customer_name=name,
            customer_phone=phone,
            quantity=qty,
            address=address,
            total_price=total,
        )

        return redirect('success')

    return render(request, 'order.html', {'product': product})


def success(request):
    return render(request, 'success.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST['full_name']
        mobile = request.POST['mobile']

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=full_name
        )

        Profile.objects.create(
            user=user,
            mobile=mobile
        )

        return redirect('login')

    return render(request, 'signup.html')



@login_required
def my_orders(request):
    # अभी dummy data (बाद में database से लेंगे)
    orders = [
        {
            'id': 101,
            'product': 'Fresh Chicken',
            'quantity': '1 Kg',
            'price': 280,
            'status': 'Pending'
        },
        {
            'id': 102,
            'product': 'Chicken Curry Cut',
            'quantity': '2 Kg',
            'price': 540,
            'status': 'Delivered'
        }
    ]
    return render(request, 'my_orders.html', {'orders': orders})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        qty = int(request.POST['quantity'])
        total = qty * product.price

        Order.objects.create(
            user=request.user,
            product=product,
            quantity=qty,
            total_price=total
        )
        return redirect('my_orders')

    return render(request, 'place_order.html', {'product': product})
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': orders})
@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    return redirect('my_orders')



def home(request):
    banners = HomeBanner.objects.all()
    return render(request, 'home.html', {'banners': banners})
