from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.notes_all, name='notes_all'),
    path('new_note/', views.new_note, name='new_note'),
    path('change_note/', views.change_note, name='change_note'),
    path('delete_note/', views.delete_note, name='delete_note'),
    path('search_note/', views.search_note, name='search_note'),
]