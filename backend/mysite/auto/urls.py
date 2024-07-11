from django.urls import path
from .views import AutoView, CarPartViewSet, CountryView

urlpatterns = [
    path('auto/', AutoView.as_view()),
    path('carpart/', CarPartViewSet.as_view({'get': 'list'})),
    path('carpart/<int:pk>', CarPartViewSet.as_view({'get': 'retrive'})),
    path('country/', CountryView.as_view()),
]
