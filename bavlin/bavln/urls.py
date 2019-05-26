
from django.urls import path
from .views import ListItemView


urlpatterns = [
    path('items/', ListItemView.as_view())
]
