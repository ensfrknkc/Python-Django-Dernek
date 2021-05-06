from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    # ex: /home/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /home/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
]