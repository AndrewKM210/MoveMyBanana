from django.urls import path

from .views import ListBoxes, CreateBox, CreateInstruction, ListInstructions, Resume, TakeProduct, PutProduct, \
    ReviewBox, CreateTest, ListProducts

urlpatterns = [
    path('view/box', ListBoxes.as_view(), name="boxes-all"),
    path('view/product', ListProducts.as_view(), name="products-all"),
    path('view/instruction', ListInstructions.as_view(), name="instructions-all"),
    path('create/box', CreateBox.as_view(), name="create-box"),
    path('create/instruction', CreateInstruction.as_view(), name="create-instruction"),
    path('resume', Resume.as_view(), name="resume"),
    path('take', TakeProduct.as_view(), name="take"),
    path('put', PutProduct.as_view(), name="put"),
    path('review', ReviewBox.as_view(), name="review"),
    path('test', CreateTest.as_view(), name="test")
]
