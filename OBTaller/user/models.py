from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # customer_id = models.CharField(max_length=100, blank=True, null=True)
    es_operador = models.BooleanField(verbose_name='Operador', default=False)
    pass