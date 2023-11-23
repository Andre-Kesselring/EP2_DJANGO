from django.urls import path

from . import views


app_name = 'lugares'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'), 
    path('search/', views.PostSearchView.as_view(), name='search'),   
    path('create/', views.PostCreateView.as_view(), name='create'), 
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),    
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category-posts/<int:category_id>/', views.CategoryPostsListView.as_view(), name='category-posts'),
    path('category-post-detail/<int:category_id>/<int:pk>/', views.CategoryPostDetailView.as_view(), name='category-post-detail'),
    path('<pk>/', views.PostDetailView.as_view(), name='detail'),
]