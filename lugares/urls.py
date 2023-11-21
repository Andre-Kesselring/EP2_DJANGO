from django.urls import path

from . import views

app_name = 'lugares'
urlpatterns = [
    path('', views.list_lugares, name='index'),
    path('search/', views.search_lugares, name='search'), 
    path('<int:lugar_id>/', views.detail_lugar, name='detail'),
    path('create/', views.create_lugar, name='create'), 
    path('update/<int:lugar_id>/', views.update_lugar, name='update'),
    path('delete/<int:lugar_id>/', views.delete_lugar, name='delete'),
]