from django.urls import path, include
from .views import StoreRegister, StoreProximity, StoreCityProximity

urlpatterns = [
    path('store/add/', StoreRegister.as_view()),
    path('store/modify/<int:pk>/', StoreRegister.as_view()),
    path('store/delete/<int:pk>/', StoreRegister.as_view()),
    path('store/nearby/zipcode/', StoreProximity.as_view()),
    path('store/nearby/city/', StoreCityProximity.as_view()),
]
