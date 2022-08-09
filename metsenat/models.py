from django.db import models
from helpers.models import BaseModel

# Create your models here.

# SPONSOR TYPE CHOICES:
INDIVIDUAL = "individual"
ENTITY = "entity"

SPONSOR_TYPE_CHOICES = (
    (INDIVIDUAL, "individual"),
    (ENTITY, "entity"),
)

# SPONSOR STATUS CHOICES:
NEW = "yangi"
IN_MODERATION = "moderatsiyada"
CONFIRMED = "tasdiqlangan"
CANCELED = "bekor qilingan"

SPONSOR_STATUS_CHOICES = (
    (NEW, "yangi"),
    (IN_MODERATION, "moderatsiyada"),
    (CONFIRMED, "tasdiqlangan"),
    (CANCELED, "bekor qilingan"),
)

# PAYMENT TYPE CHOICES:
UZCARD = "uzcard"
HUMO = "humo"
VISA = "visa"
CASH = 'cash'

PAYMENT_TYPE_CHOICES = (
    (UZCARD, "uzcard"),
    (HUMO, "humo"),
    (VISA, "visa"),
    (CASH, "cash"),
)

# STUDENT TYPE CHOICES:
BACHELOR = "bakalavr"
MASTERS = "magistr"

STUDENT_TYPE_CHOICES = (
    (BACHELOR, "bakalavr"),
    (MASTERS, "magistr")
)


# SPONSOR:
class Sponsor(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True, null=True, blank=True)
    sponsor_type = models.CharField(max_length=100, choices=SPONSOR_TYPE_CHOICES, default=SPONSOR_TYPE_CHOICES[1][0])
    phone_number = models.CharField(max_length=128)
    balance = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    company_name = models.CharField(max_length=128, null=True, blank=True)

    register_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=SPONSOR_STATUS_CHOICES, default=SPONSOR_STATUS_CHOICES[0][0])
    spent_amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    payment_type = models.CharField(max_length=100, choices=PAYMENT_TYPE_CHOICES, default=SPONSOR_STATUS_CHOICES[3][0])

    def __str__(self):
        return self.name


# UNIVERSITY:
class University(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


# STUDENT:
class Student(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True, null=True, blank=True)
    student_type = models.CharField(max_length=100, choices=STUDENT_TYPE_CHOICES)
    received_amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    tuition_fee = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    phone_number = models.CharField(max_length=128)

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students')


# STUDENT SPONSOR:
class StudentSponsor(BaseModel):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='students')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sponsors')
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
