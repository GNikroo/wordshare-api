from django.urls import path
from posts import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/delete-image/', views.DeleteImageView.as_view()),
]
