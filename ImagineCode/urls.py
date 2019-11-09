from django.urls import path
from rest_framework import request

from .views import ListBoxes, CreateBox, CreateInstruction, ListInstructions, Resume

urlpatterns = [
    path('view/box', ListBoxes.as_view(), name="boxes-all"),
    path('view/instruction', ListInstructions.as_view(), name="instructions-all"),
    path('create/box', CreateBox.as_view(), name="create-box"),
    path('create/instruction', CreateInstruction.as_view(), name="create-instruction"),
    path('resume', Resume.as_view(), name="resume")

]
