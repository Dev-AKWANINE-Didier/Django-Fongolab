from django.urls import path  
from app1.views import index



urlpatterns = [
    path(route="home/<int:name>/", view=index, name="home")
]
