from rest_framework import serializers
from .models import Sponsor


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
