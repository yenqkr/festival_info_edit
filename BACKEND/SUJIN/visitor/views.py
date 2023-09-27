from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Visitor
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
    visitor_list = Visitor.objects.all().order_by('-date')
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