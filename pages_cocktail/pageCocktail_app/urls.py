from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page_2', views.p2, name='page2'),
    path('page_3', views.p3, name='page3'),
    path('page_4', views.p4, name='page4'),
    path('page_5', views.p5, name='page5'),
]
