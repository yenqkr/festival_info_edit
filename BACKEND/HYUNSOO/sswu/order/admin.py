from django.contrib import admin
from .models import Goods, Reservation, OrderItem
from django.contrib.auth.models import PermissionsMixin

class OrderItemInline(admin.TabularInline):  
    model = OrderItem
    extra = 1  

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone_number', 'user_mail', 'get_goods_name', 'get_total_price','reserved_at']
    inlines = [OrderItemInline]

    def get_goods_name(self, obj):
        return ", ".join([item.goods.name for item in obj.item.all()])
    
    def get_total_price(self, obj):
        return sum([item.goods.price * item.quantity for item in obj.item.all()])

    get_goods_name.short_description = "굿즈 이름"
    get_total_price.short_description = "총 가격"

    list_filter = ['item__goods__name',]
    search_fields = ['user_name','phone_number','user_mail',]

class Selected_Goods(admin.ModelAdmin):
    list_display = ['name', 'price']

#admin.site.register(OrderItem)  
admin.site.register(Goods, Selected_Goods)
admin.site.register(Reservation, ReservationAdmin)
