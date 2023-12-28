from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail-post'),
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('<int:pk>/update/', views.UpdatePostView.as_view(), name='update-post'),
    path('<int:pk>/delete/', views.DeletePostView.as_view(), name='delete-post'),
]
