from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Cart, CartItem


def home(request):
    """Home page with featured products"""
    featured_products = Product.objects.filter(available=True).order_by('-created_at')[:8]
    categories = Category.objects.all()
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'store/home.html', context)


def product_list(request):
    """Product listing page with filtering"""
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    # Filter by gender
    gender = request.GET.get('gender')
    if gender:
        products = products.filter(gender=gender)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
    
    # Sort products
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'newest':
        products = products.order_by('-created_at')
    else:
        products = products.order_by('name')
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
        'current_gender': gender,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'store/product_list.html', context)


def product_detail(request, slug):
    """Product detail page"""
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'store/product_detail.html', context)


def get_or_create_cart(request):
    """Helper function to get or create cart"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


def add_to_cart(request, product_id):
    """Add product to cart"""
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id, available=True)
        quantity = int(request.POST.get('quantity', 1))
        
        cart = get_or_create_cart(request)
        
        # Check if product already in cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        messages.success(request, f'{product.name} added to cart!')
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'{product.name} added to cart!',
                'cart_total': cart.total_items
            })
        
        return redirect('store:cart')
    
    return redirect('store:product_list')


def remove_from_cart(request, item_id):
    """Remove item from cart"""
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart = cart_item.cart
        
        # Check if user owns this cart
        if (request.user.is_authenticated and cart.user == request.user) or \
           (not request.user.is_authenticated and cart.session_key == request.session.session_key):
            cart_item.delete()
            messages.success(request, 'Item removed from cart!')
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Refresh cart to get updated totals
            cart.refresh_from_db()
            return JsonResponse({
                'success': True,
                'message': 'Item removed from cart!',
                'cart_total': cart.total_items,
                'cart_total_price': cart.total_price
            })
    
    return redirect('store:cart')


def update_cart_quantity(request, item_id):
    """Update cart item quantity"""
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart = cart_item.cart
        
        # Check if user owns this cart
        if (request.user.is_authenticated and cart.user == request.user) or \
           (not request.user.is_authenticated and cart.session_key == request.session.session_key):
            quantity = int(request.POST.get('quantity', 1))
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            else:
                cart_item.delete()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Refresh cart to get updated totals
            cart.refresh_from_db()
            return JsonResponse({
                'success': True,
                'cart_total': cart.total_items,
                'item_total': cart_item.total_price,
                'cart_total_price': cart.total_price
            })
    
    return redirect('store:cart')


def cart_view(request):
    """Cart page"""
    cart = get_or_create_cart(request)
    
    context = {
        'cart': cart,
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    """Checkout page"""
    cart = get_or_create_cart(request)
    
    if cart.total_items == 0:
        messages.warning(request, 'Your cart is empty!')
        return redirect('store:cart')
    
    context = {
        'cart': cart,
    }
    return render(request, 'store/checkout.html', context) 