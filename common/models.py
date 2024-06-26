from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class Usuario(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    is_persona = models.BooleanField(default=False)
    is_organizacion = models.BooleanField(default=False)

