from django.shortcuts import render
from rest_framework import generics
from .models import Sponsor
from .serializer import RegisterSponsorSerializer, ListSponsorsSerializer
from helpers.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# REGISTER SPONSOR:
class RegisterSponsorView(generics.ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = RegisterSponsorSerializer
    pagination_class = CustomPagination

    permission_classes = [IsAuthenticated]


# LIST SPONSORS:
class ListSponsorsView(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = ListSponsorsSerializer
    pagination_class = CustomPagination
