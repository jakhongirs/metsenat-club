from django.shortcuts import render
from rest_framework import generics
from .models import Sponsor, Student, University
from .serializer import RegisterSponsorSerializer, ListSponsorsSerializer, DetailSponsorSerializer, \
    UpdateSponsorSerializer, RegisterStudentSerializer, CreateUniversitySerializer, ListStudentsSerializer, \
    DetailStudentSerializer
from helpers.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework


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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('status', 'balance')
    search_fields = ('name',)


# DETAIL SPONSOR:
class DetailSponsorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = DetailSponsorSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset


# UPDATE SPONSOR:
class UpdateSponsorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = UpdateSponsorSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset


# CREATE UNIVERSITY:
class CreateUniversityView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = CreateUniversitySerializer
    pagination_class = CustomPagination

    permission_classes = [IsAuthenticated]


# REGISTER STUDENT:
class RegisterStudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = RegisterStudentSerializer
    pagination_class = CustomPagination

    permission_classes = [IsAuthenticated]


# LIST STUDENT:
class ListStudentsView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = ListStudentsSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('student_type', 'university')
    search_fields = ('name',)


# DETAIL STUDENT:
class DetailStudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = DetailStudentSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset
