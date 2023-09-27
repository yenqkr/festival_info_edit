from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Info, InfoImage
from .forms import InfoForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# 메인페이지
def mainpage(request):
    return render(request, 'mainpage.html')

def makers(request):
    return render(request, 'makers.html')

# 관리자 로그인
def administrator(request):
    if request.method == 'POST':
        username = request.POST['custom_id']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 로그인 성공시 메인페이지로 이동
            return redirect('mainpage:mainpage')
        else:
            return render(request, 'administrator.html', {'error': 'username or password is incorrect.'})
    return render(request, 'administrator.html')


# info 목록 
# 더보기를 눌렀을 때 6개씩 더 보이기
def info_list(request):
    page = request.GET.get('page', 1)
    infos = Info.objects.all()
    return render(request, 'info.html', {'infos': infos})


# info 작성 처리
@login_required()
def info_write(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            info = Info()
            info.title = form.cleaned_data['title']
            info.content = form.cleaned_data['content']
            info.save() 
            for i in request.FILES.getlist('images'):
                InfoImage.objects.create(info=info, image=i)
            # 작성 완료 후 info 목록으로 이동
            return redirect('mainpage:info')
    else:
        form = InfoForm()
    return render(request, 'info_write.html', {'form': form})

# info 상세보기
def info_post(request, info_id):
    info = get_object_or_404(Info, pk=info_id)
    return render(request, 'info_post.html', {'info': info})
