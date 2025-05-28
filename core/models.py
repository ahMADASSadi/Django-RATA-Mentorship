from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models


from core.validators import PHONE_NUMBER_VALIDATOR


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Created at: {self.created_at}, Updated at: {self.updated_at}"
    
    class Meta:
        abstract = True


# class User(BaseUser):
#     telegram_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
#     phone_number = models.CharField(
#         max_length=11,
#         unique=True,
#         null=True,
#         blank=True,
#         validators=[PHONE_NUMBER_VALIDATOR],
#     )

#     def __str__(self):
#         return f"{self.username}->{self.email}"
