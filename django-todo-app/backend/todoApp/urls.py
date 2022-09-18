from django.urls import path
from . import views

urlpatterns = [
    # path('', views.TestView, name='test_view'),
    path('', views.index_view, name='index_view'),
    path('add_todo/', views.add_todo, name='add_todo'),
]