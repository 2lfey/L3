from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/comment', views.CreateComment.as_view(), name='create-comment'),
    path('<int:post_pk>/comments/<int:pk>/delete', views.DeleteComment.as_view(), name='delete-comment'),
    path('<int:post_pk>/comments/<int:pk>/update', views.UpdateComment.as_view(), name='update-comment'),
]
