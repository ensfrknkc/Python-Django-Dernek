from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from contents.models import Menu, Content, Images, Comment

class ContentImageInline(admin.TabularInline):
    model = Images
    extra = 5

class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']




class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','menu' , 'type', 'image_tag','status','user']
    list_filter = ['status' , 'type']
    inlines = [ContentImageInline]
    prepopulated_fields = {'slug': ('title',)}

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title' , 'content', 'image_tag']
    readonly_fields = ('image_tag',)

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Menu.objects.add_related_count(
                qs,
                Content,
                'menu',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Menu.objects.add_related_count(qs,
                 Content,
                 'menu',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related Content (for this specific Menu)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related Content (in tree)'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','content','user','status']
    list_filter = ['status']

admin.site.register(Menu,CategoryAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)




