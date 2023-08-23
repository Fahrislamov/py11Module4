from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','created_date','negotiable','updated_date', 'user','image_display']
    list_filter = ['negotiable', 'created_at']
    actions = ['make_negotiables_as_false','make_negotiables_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description','image', 'user'),
            'classes':['collapse']
        }),
        ('Финансы',{
            'fields': ('price','negotiable'),
            'classes':['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_negotiables_as_false(self,request,queryset):
        queryset.update(negotiable=False)

    @admin.action(description='Добавить возможность торга')
    def make_negotiables_as_true(self,request,queryset):
        queryset.update(negotiable=True)

admin.site.register(Advertisements,AdvertisementAdmin)

