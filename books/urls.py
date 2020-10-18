from django.urls import path

from books import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('', views.index, name='index')

]
