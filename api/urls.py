from django.urls import path
from . import views

urlpatterns = [
    path('video/<int:post_id>', views.video),
]
