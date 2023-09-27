from django.shortcuts import render, redirect
from order.forms import ReservationForm
from .models import Goods, Reservation, OrderItem
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse

def goods_list(request):
    goods = Goods.objects.all()

    if request.method == 'POST':
        selected_goods = {} 
        total_price = 0

        for good in goods:
            quantity_key = f"quantity_{good.id}"
            if quantity_key in request.POST and request.POST[quantity_key]:
                quantity = int(request.POST[quantity_key])
                total_price += quantity * good.price
                selected_goods[good.name] = {
                    'price': good.price,
                    'quantity': quantity,
                }

        request.session['selected_goods'] = selected_goods
        request.session['total_price'] = total_price
        return redirect('order:reserve')
    else:
        return render(request, 'goods_list.html', {'goods': goods})

def reserve_goods(request):
    selected_goods_data = request.session.get('selected_goods', {})

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()

            for good_name, data in selected_goods_data.items():
                good = Goods.objects.get(name=good_name)
                OrderItem(reservation=reservation, goods=good, quantity=data['quantity']).save()

            messages.success(request, '예약이 완료되었습니다.')
            request.session['reservation_complete'] = True
            del request.session['selected_goods']

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ReservationForm()
        total_price = sum([data['price'] * data['quantity'] for data in selected_goods_data.values()])
        return render(request, 'reserve.html', {'form': form, 'selected_goods': selected_goods_data, 'total_price': total_price})

def home(request):
    return render(request, 'home.html')