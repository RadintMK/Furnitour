from django.shortcuts import render, get_object_or_404, redirect
from.models import Tour,Cart
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid

def index(request):
    return render(request, 'main/index.html')

def aboutus(request):
    return render(request, 'main/aboutus.html')

def tours(request):
    tours = Tour.objects.all()
    return render(request, 'main/tours.html',{'tours': tours})

def cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart_items = Cart.objects.filter(session_id=cart_id)
    else:
        cart_items = []

    return render(request, 'main/cart.html', {'cart_items': cart_items})

def pay(request, tour_name):
    tour = get_object_or_404(Tour, title=tour_name)
    cost = tour.price_from
    
    context = {
        'cost': cost,
    }
    
    return render(request, 'main/pay.html', context)

def tour_info(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    context = {
        'tour': tour,
    }
    return render(request, 'tourInfo.html', context)

def tourInfo(request, tour_name):
    tour = get_object_or_404(Tour, title=tour_name)
    return render(request, 'main/tourInfo.html', {'tour': tour})


@csrf_exempt
def add_to_cart(request, tour_name):
    try:
        tour = Tour.objects.get(title=tour_name)
    except Tour.DoesNotExist:
        return JsonResponse({'error': 'Тур не найден'}, status=404)

    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart_id = str(uuid.uuid4())
        request.session['cart_id'] = cart_id

    Cart.objects.create(tour=tour, session_id=cart_id)

    return redirect('cart')