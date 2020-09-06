from django.urls import path, include
from .views import StoreRequestView, CustomerRequestView
urlpatterns = [
    path('request/create/<str:pk>/', CustomerRequestView.as_view()), #store id
    path('request/delete/<str:pk>/', CustomerRequestView.as_view()), #itemrequest id
    path('request/view/<str:pk>/', StoreRequestView.as_view()), #store id
    path('request/fulfill/<str:pk>/', StoreRequestView.as_view()), #itemrequest id
    path('requests/customerview/', CustomerRequestView.as_view()) #customer id through header
]