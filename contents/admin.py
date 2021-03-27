from django.contrib import admin

# Register your models here.
from contents.models import Menu
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

admin.site.register(Menu,MenuAdmin)
