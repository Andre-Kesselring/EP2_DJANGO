from django.urls import path

from . import views


app_name = 'lugares'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'), 
    path('search/', views.PostSearchView.as_view(), name='search'),  
    path('<int:lugar_id>/', views.PostDetailView.as_view(), name='detail'), 
    path('create/', views.PostCreateView.as_view(), name='create'), 
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
]