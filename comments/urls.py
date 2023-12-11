from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/comment', views.CreateComment.as_view(), name='create-comment'),
]
