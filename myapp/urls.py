from django.urls import path
from .views import MyModelAPIView

urlpatterns = [
    path('my-model/', MyModelAPIView.as_view(), name='my-model-list'),
 
]
