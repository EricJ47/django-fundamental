from django.db import models


class Member(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    no_telp = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100)