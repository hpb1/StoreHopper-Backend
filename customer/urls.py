from django.urls import path, include
from .views import StoreRequestView, CustomerRequestView
urlpatterns = [
    path('request/create/<int:pk/', CustomerRequestView.as_view()), #store id
    path('request/delete/<int:pk/', CustomerRequestView.as_view()), #request id
    path('request/view/<int:pk/', StoreRequestView.as_view()) #store id
]