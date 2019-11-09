from django.urls import path
from rest_framework import request

from .views import ListBoxes, CreateBox


urlpatterns = [
    path('view', ListBoxes.as_view(), name="boxes-all"),
    path('create', CreateBox.as_view(), name="create-box")
]
