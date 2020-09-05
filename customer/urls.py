from django.urls import path, include
from .views import StoreRequestView, CustomerRequestView
urlpatterns = [
    path('request/create/<str:pk/', CustomerRequestView.as_view()), #store id
    path('request/delete/<str:pk/', CustomerRequestView.as_view()), #request id
    path('request/view/<str:pk>/', StoreRequestView.as_view()) #store id
]