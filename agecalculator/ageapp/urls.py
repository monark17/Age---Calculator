from django.urls import path
from .views import age_calculator

urlpatterns = [
    path('', age_calculator, name='age_calculator'),
]
