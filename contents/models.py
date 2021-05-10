from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Select, FileInput
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self',blank=True, null=True , related_name='children' , on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return ' / '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse('menu_detail', kwargs={'slug': self.slug})

#image_tag ıda eklemeyi dene

TYPE = (
        ('Menu', 'Menu'),
        ('News', 'Haber'),
        ('Notice', 'Duyuru'),
    )
class Content(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE,blank=True,null=True) #relation with Menu
    user = models.ForeignKey(User, on_delete=models.CASCADE,)  # relation with User
    title = models.CharField(max_length=100)
    keywords = models.CharField(blank=True,max_length=255)
    description = models.CharField(blank=True,max_length=255)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(null=False, unique=True)
    detail = RichTextUploadingField()
    type = models.CharField(max_length=10, choices=TYPE)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('content_detail', kwargs={'slug': self.slug})


class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'slug', 'keywords', 'description', 'type', 'image' , 'detail']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control mb-30', 'placeholder': 'title'}),
            'slug': TextInput(attrs={'class': 'form-control mb-30', 'placeholder': 'slug'}),
            'keywords': TextInput(attrs={'class': 'form-control mb-30', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'form-control mb-30', 'placeholder': 'description'}),
            'type': Select(attrs={'class': 'form-control mb-30', 'placeholder': 'type'},choices=TYPE),
            'image': FileInput(attrs={'class': 'form-control mb-30', 'placeholder': 'image'}),
            'detail': CKEditorWidget(), #Ckeditör input
        }

class Images(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class ContentImageForm(ModelForm):
    class Meta:
        model = Images
        fields = ['title', 'image']

class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    content = models.ForeignKey(Content, on_delete=models.CASCADE)  # relation with Content
    user = models.ForeignKey(User, on_delete=models.CASCADE, )  # relation with User
    subject = models.CharField(max_length=100)
    comment = models.TextField(max_length=200,blank=True)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(max_length=20,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate', ]

