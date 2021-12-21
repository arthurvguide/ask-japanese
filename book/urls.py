from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingView.as_view(), name='book'),
]