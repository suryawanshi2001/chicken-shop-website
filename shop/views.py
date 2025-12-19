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
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Order
from django.shortcuts import redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required


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

# CUSTOMER MY ORDERS
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': orders})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # ✅ ADMIN
            if user.is_staff:
                return redirect('/admin-dashboard/')

            # ✅ CUSTOMER
            return redirect('/')

        else:
            return render(request, 'login.html', {'error': 'Invalid login'})

    return render(request, 'login.html')
# CUSTOMER SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'signup.html')


# CUSTOMER LOGIN
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


# CUSTOMER LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')

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

@staff_member_required
def admin_dashboard(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard.html', {'orders': orders})




@staff_member_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        order.status = request.POST['status']
        order.save()

    return redirect('/admin-dashboard/')
