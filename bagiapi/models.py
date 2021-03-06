from django.db import models
from django.core.files.storage import FileSystemStorage

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

    class Meta:
        verbose_name_plural = 'users'
    
    def __str__(self):
        return self.email


class ProfileGuru(models.Model):
    """
    Profile guru model
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    nuptk = models.CharField(max_length=150, blank=True)
    institusi = models.CharField(max_length=200, blank=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    nomor = models.CharField(max_length=100, blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}"


class ProfileMurid(models.Model):
    """
    Profile murid model
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    sekolah = models.CharField(max_length=100, blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    no_induk = models.CharField(max_length=100, blank=True, null=True)
    nomor = models.CharField(max_length=100, blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    reward = models.IntegerField(blank=True, null=True)
    jumlahcourse = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}"


class Course(models.Model):
    """
    Course Model
    """
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    judul = models.CharField(max_length=200)
    # materi = models.FileField(upload_to='materi_course/')
    deskripsi = models.TextField(blank=True, null=True)
    link = models.URLField()
    reward = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ManyToManyField(ProfileMurid, through='Enrollment')
    # material = models.ForeignKey(Material)
    def __str__(self):
        return self.judul


class Material(models.Model):
    """
    material model
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pertemuan = models.CharField(max_length=50, blank=True, null=True)
    link = models.URLField(blank=True)
    modul = models.FileField(upload_to='modul_course/')

    def __str__(self):
        return self.pertemuan


class Enrollment(models.Model):
    """
    student enroll model
    """

    user = models.ForeignKey(ProfileMurid, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    reward = models.IntegerField(blank=True, null=True)


    class Meta:
        unique_together = [['user','course']]

    
    def __str__(self):
        return f"{ self.user } : { self.course }"