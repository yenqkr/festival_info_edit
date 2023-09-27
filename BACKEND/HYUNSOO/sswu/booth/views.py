from django.shortcuts import render
from .models import Booth
from django.db.models import Q,F,Case, When, Value, CharField, IntegerField,ExpressionWrapper
from django.db.models.functions import Cast
from django.db.models.functions import Substr

def boothinfo(request):
    if request.method == 'GET':
        booth_list = Booth.objects.all().annotate(
    prefix=ExpressionWrapper(
        Substr(F('locate'), 1, 1),  # 'locate' 필드의 첫 번째 문자 추출
        output_field=CharField()
    ),
    numeric_locate=ExpressionWrapper(
        Case(
            When(prefix='A', then=Value(1)),  
            When(prefix='B', then=Value(2)),  
            When(prefix='C', then=Value(3)),  
            When(prefix='D', then=Value(4)),  
            When(prefix='E', then=Value(5)),  
            When(prefix='F', then=Value(6)),  
            default=Value(0),  # 다른 경우 0으로 설정하거나 다른 기본값 사용
            output_field=IntegerField()
        ) * 1000 +  # 여기서 1000을 곱해 "a", "b", "e"를 구분하고, 각 그룹 내에서 숫자를 정렬합니다.
        Cast(Substr(F('locate'), 3), IntegerField()),  # 문자열의 세 번째 문자부터 추출하여 정수로 변환
        output_field=IntegerField()
    )
).order_by('numeric_locate')
        context = {
            'booth_list' : booth_list
        }
        return render(request, 'boothinfo.html', context)
    else:
        #검색어
        if 'search' in request.POST:
            searched = request.POST['search']    
            booth_list = Booth.objects.filter(name__icontains=searched).annotate(
            prefix=ExpressionWrapper(
                Substr(F('locate'), 1, 1),  # 'locate' 필드의 첫 번째 문자 추출
                output_field=CharField()
            ),
            numeric_locate=ExpressionWrapper(
                Case(
                    When(prefix='A', then=Value(1)),  
                    When(prefix='B', then=Value(2)),  
                    When(prefix='C', then=Value(3)),  
                    When(prefix='D', then=Value(4)),  
                    When(prefix='E', then=Value(5)),  
                    When(prefix='F', then=Value(6)),  
                    default=Value(0),  # 다른 경우 0으로 설정하거나 다른 기본값 사용
                    output_field=IntegerField()
                ) * 1000 +  # 여기서 1000을 곱해 "a", "b", "e"를 구분하고, 각 그룹 내에서 숫자를 정렬합니다.
                Cast(Substr(F('locate'), 3), IntegerField()),  # 문자열의 세 번째 문자부터 추출하여 정수로 변환
                output_field=IntegerField()
            )
        ).order_by('numeric_locate')
            context = {
                'booth_list' : booth_list
            }
            return render(request, 'boothinfo.html', context)
        else:
            #필터
            date = request.POST.getlist('date', None)
            time = request.POST.getlist('time', None)
            kind = request.POST.getlist('kind', None)

            q=Q()
            if date:
                # q &= Q(date__icontains=date)
                for data in date:
                    cleaned_date = data.replace(" ", "").lower()  # 데이터 정제 및 비교
                    q &= Q(date__icontains=cleaned_date)
            if time:
                for dataa in time:
                    cleaned_datee = dataa.replace(" ", "").lower()  # 데이터 정제 및 비교
                    q &= Q(time__icontains=cleaned_datee)
            if kind:
                q &= Q(kind__in = kind)
                        
            booth_list = Booth.objects.filter(q).annotate(
            prefix=ExpressionWrapper(
                Substr(F('locate'), 1, 1),  # 'locate' 필드의 첫 번째 문자 추출
                output_field=CharField()
            ),
            numeric_locate=ExpressionWrapper(
                Case(
                    When(prefix='A', then=Value(1)),  
                    When(prefix='B', then=Value(2)),  
                    When(prefix='C', then=Value(3)),  
                    When(prefix='D', then=Value(4)),  
                    When(prefix='E', then=Value(5)),  
                    When(prefix='F', then=Value(6)),  
                    default=Value(0),  # 다른 경우 0으로 설정하거나 다른 기본값 사용
                    output_field=IntegerField()
                ) * 1000 +  # 여기서 1000을 곱해 "a", "b", "e"를 구분하고, 각 그룹 내에서 숫자를 정렬합니다.
                Cast(Substr(F('locate'), 3), IntegerField()),  # 문자열의 세 번째 문자부터 추출하여 정수로 변환
                output_field=IntegerField()
            )
        ).order_by('numeric_locate')
            context = {
                'booth_list' : booth_list
            }
            return render(request, 'boothinfo.html', context)
    
