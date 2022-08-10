from rest_framework import serializers
from .models import Sponsor, Student, University, StudentSponsor


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


# CREATE STUDENT SPONSOR:
class StudentSponsorSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['amount'] > attrs['sponsor'].balance:
            raise serializers.ValidationError({
                'amount': "Kiritilgan summa sponsorning balansidan kichik bo'lishi kerak"
            })

        if attrs['amount'] + attrs['student'].received_amount > attrs['student'].tuition_fee:
            raise serializers.ValidationError({
                'amount': "Talabaga ajratilayotgan summa kontrakt summasidan kichik bo'lishi kerak!"
            })

        return attrs

    class Meta:
        model = StudentSponsor
        fields = ('sponsor', 'student', 'amount')


# UPDATE STUDENT SPONSOR:
class UpdateStudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ('sponsor', 'student', 'amount')


# DETAIL STUDENT SPONSOR:
class DetailStudentSponsorSerializer(serializers.ModelSerializer):
    sponsor = ListSponsorsSerializer()

    class Meta:
        model = StudentSponsor
        fields = ('sponsor', 'amount')


# DETAIL STUDENT:
class DetailStudentSerializer(serializers.ModelSerializer):
    university = CreateUniversitySerializer()
    sponsors = DetailStudentSponsorSerializer(many=True)

    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'university', 'student_type', 'received_amount', 'tuition_fee', 'sponsors')


# UPDATE STUDENT:
class UpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'university', 'tuition_fee')


# DASHBOARD LINE STUDENTS CHART:
class LineDashboardStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'created_at')


# DASHBOARD LINE SPONSORS CHART:
class LineDashboardSponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'created_at')
