from django.shortcuts import render
from rest_framework import generics
from .models import Sponsor, Student, University, StudentSponsor
from .serializer import RegisterSponsorSerializer, ListSponsorsSerializer, DetailSponsorSerializer, \
    UpdateSponsorSerializer, RegisterStudentSerializer, CreateUniversitySerializer, ListStudentsSerializer, \
    DetailStudentSerializer, UpdateStudentSerializer, StudentSponsorSerializer, UpdateStudentSponsorSerializer, \
    LineDashboardSponsorsSerializer, LineDashboardStudentsSerializer
from helpers.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework
from django.db import models
from rest_framework.response import Response


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


# UPDATE STUDENT:
class UpdateStudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = UpdateStudentSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset


# CREATE STUDENT SPONSOR:
class CreateStudentSponsorView(generics.CreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    pagination_class = CustomPagination

    permission_classes = [IsAuthenticated]


# UPDATE STUDENT SPONSOR:
class UpdateStudentSponsorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = UpdateStudentSponsorSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset


# LIST DASHBOARD DATA:
class DashboardData(generics.ListAPIView):
    serializer_class = UpdateStudentSponsorSerializer
    pagination_class = CustomPagination

    def get(self, request, format=None):
        total_spent = Sponsor.objects.aggregate(total_sponsors_spent=models.Sum('spent_amount'))
        total_tuition_fee = Student.objects.aggregate(total_tuition_fee=models.Sum('tuition_fee'))

        total_spent = total_spent['total_sponsors_spent']
        total_tuition_fee = total_tuition_fee['total_tuition_fee']

        required_amount = total_tuition_fee - total_spent

        return Response({'total_sponsors_spent': total_spent,
                         'total_tuition_fee': total_tuition_fee,
                         'required_amount': required_amount})


# LINE DASHBOARD STUDENT DATA:
class DashboardLineStudent(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = LineDashboardStudentsSerializer
    pagination_class = CustomPagination


# LINE DASHBOARD SPONSOR DATA:
class DashboardLineSponsor(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = LineDashboardSponsorsSerializer
    pagination_class = CustomPagination
