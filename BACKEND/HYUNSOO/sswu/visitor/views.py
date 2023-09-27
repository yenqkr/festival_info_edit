from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Visitor
from django.http import JsonResponse

# Create your views here.
def visitor_write(request):
    if request.method == 'GET':
        return render(request, 'visitor-write.html')
    else:
        content = request.POST.get('content')
        nickname = request.POST.get('nickname')
        code = request.POST.get('code')
        Visitor.objects.create(
            nickname=nickname,
            content = content,
            code = code,
        )
        return redirect('/visitor')
    
def visitor(request):
    visitor_list = Visitor.objects.all().order_by('-date')[:10]
    context = {
        'visitor_list' : visitor_list
    }
    return render(request, 'visitor.html', context)

def visitor_more(request):
    visitor_list = Visitor.objects.all().order_by('-date')
    context = {
        'visitor_list' : visitor_list
    }
    return render(request, 'visitor.html', context)

def visitor_json(request):
    current_page = int(request.GET.get('page'))
    items_per_page = int(request.GET.get('items_per_page'))
    visitor_list = Visitor.objects.all().order_by('-date')[
        (current_page-1)*items_per_page:current_page*items_per_page]
    visitor_json = [
        {"content": visitor.content, "nickname": visitor.nickname, "code": visitor.code, "date": visitor.date.strftime("%Y-%m-%d %H:%M:%S")} for visitor in visitor_list
    ]
    context = {
        'visitor_list': visitor_json
    }
    return JsonResponse(context)