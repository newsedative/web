from django.urls import path
from .views import AutoView

urlpatterns = [
    path('auto/', AutoView.as_view()),
]
