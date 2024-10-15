from django.urls import path
from pages import views


app_name = 'pages'

urlpatterns = [
    path('contact/', views.ContentView.as_view(), name='contact'),
]