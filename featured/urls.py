from django.urls import path
from featured import views


urlpatterns = [
    path('featured/', views.Featured.as_view()),
    path('featured/<int:pk>/', views.FeaturedDetail.as_view()),
]
