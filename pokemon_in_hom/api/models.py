from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
# Create your models here.

class SocialUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True,
                          is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField('email address',  unique=True, db_index=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = SocialUserManager()

    def __str__(self):
        return self.email