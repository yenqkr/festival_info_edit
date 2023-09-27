from django.contrib import admin
from .models import Info, InfoImage

class InfoImageInline(admin.TabularInline):
    model = InfoImage
    extra = 1

class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    inlines = [InfoImageInline]

admin.site.register(Info, InfoAdmin)
admin.site.register(InfoImage)