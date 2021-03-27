from django.contrib import admin

# Register your models here.
from contents.models import Menu, Content


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title' , 'type', 'status']
    list_filter = ['status' , 'type']

admin.site.register(Menu,MenuAdmin)
admin.site.register(Content,ContentAdmin)




