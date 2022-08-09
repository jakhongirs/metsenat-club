from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    INVALID_CODE = "######"

    full_name = models.CharField(_("full name"), max_length=256)

    created_at = models.DateTimeField(_("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_("date updated"), auto_now=True)

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("user")
        verbose_name_plural = _("users")
