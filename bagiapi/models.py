from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    """
    override django user model with custom setting
    change username field to email field
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class ProfileGuru(models.Model):
    """
    Profile guru model
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    nuptk = models.CharField(max_length=150, blank=True)
    institusi = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user

class Course(models.Model):
    """
    Course Model
    """
    judul = models.CharField(max_length=200)
    materi = models.TextField()
    link = models.URLField()
    reward = models.IntegerField()

    def __str__(self):
        return self.judul
