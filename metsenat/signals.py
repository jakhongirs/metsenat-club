from django.dispatch import receiver
from django.db.models.signals import post_save

from metsenat.models import StudentSponsor
from metsenat.models import Sponsor, Student


@receiver(post_save, sender=StudentSponsor)
def add_amount(sender, instance, created, **kwargs):
    if created:
        sponsor = instance.sponsor
        sponsor.balance -= instance.amount
        sponsor.spent_amount += instance.amount
        sponsor.save()

        student = instance.student
        student.received_amount += instance.amount
        student.save()

        print(student.received_amount)
