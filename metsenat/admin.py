from django.contrib import admin
from metsenat.models import Student, Sponsor, University, StudentSponsor

# Register your models here.
admin.site.register(Student)
admin.site.register(Sponsor)
admin.site.register(University)
admin.site.register(StudentSponsor)
