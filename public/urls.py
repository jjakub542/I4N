from django.urls import path
from .views import homepage, wypowiedzi

urlpatterns = [
    path("", homepage, name="homepage"),
    path("wypowiedzi", wypowiedzi, name="wypowiedzi"),
]
