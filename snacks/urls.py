from django.urls import path
from snacks.api.viewset import SnackListAPIView, SnacksDetailAPIView

urlpatterns = [
    path('api/v1/snacks-list', SnackListAPIView.as_view(), name='snacks_list'),
    path('api/v1/<int:pk>', SnacksDetailAPIView.as_view(), name='snack_detail'),
]   