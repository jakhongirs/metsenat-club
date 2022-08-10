from rest_framework import serializers
from .models import Sponsor, Student, University


# REGISTER SPONSOR:
class RegisterSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'sponsor_type', 'phone_number', 'balance', 'company_name')


# LIST SPONSORS:
class ListSponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'phone_number', 'balance', 'spent_amount', 'register_datetime', 'status')


# DETAIL SPONSOR:
class DetailSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'phone_number', 'balance', 'status', 'company_name')


# UPDATE SPONSOR:
class UpdateSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'sponsor_type', 'phone_number', 'balance', 'status', 'payment_type', 'company_name')


# CREATE UNIVERSITY:
class CreateUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)


# REGISTER STUDENT:
class RegisterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'university', 'student_type', 'tuition_fee')


# LIST STUDENTS:
class ListStudentsSerializer(serializers.ModelSerializer):
    university = CreateUniversitySerializer()

    class Meta:
        model = Student
        fields = ('name', 'student_type', 'university', 'received_amount', 'tuition_fee')
