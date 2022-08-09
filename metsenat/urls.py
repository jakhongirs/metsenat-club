from django.urls import path
from metsenat import views

urlpatterns = [
    path("sponsor/register/", views.RegisterSponsorView.as_view(), name="register_sponsor"),
    path("sponsors/", views.ListSponsorsView.as_view(), name="sponsors"),
]
