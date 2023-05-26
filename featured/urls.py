from django.urls import path
from featured import views

urlpatterns = [
    path('featured/', views.RandomFeaturedPost.as_view()),
]
