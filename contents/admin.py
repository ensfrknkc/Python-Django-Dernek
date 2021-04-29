from django.contrib import admin

# Register your models here.
from contents.models import Menu, Content, Images

class ContentImageInline(admin.TabularInline):
    model = Images
    extra = 5

class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title' , 'type', 'status','image_tag','user']
    readonly_fields = ('image_tag',)
    list_filter = ['status' , 'type']
    inlines = [ContentImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title' , 'content', 'image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Menu,MenuAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Images,ImagesAdmin)




