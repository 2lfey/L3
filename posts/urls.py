from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    # path('<int:pk>/edit/', views.EditPostView.as_view(), name='edit-post'),
    # path('<int:pk>/delete/', views.DeletePostView.as_view(), name='delete-post'),
]
