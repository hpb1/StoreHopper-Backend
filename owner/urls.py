from django.urls import path, include
from .views import StoreRegister, StoreProximity, StoreCityProximity

urlpatterns = [
    path('add/', StoreRegister.as_view()),
    path('modify/<str:pk>/', StoreRegister.as_view()),
    path('delete/<str:pk>/', StoreRegister.as_view()),
    path('nearby/zipcode/', StoreProximity.as_view()),
    path('nearby/city/', StoreCityProximity.as_view()),
]
