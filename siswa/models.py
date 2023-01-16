from django.db import models
from django.utils.translation import gettext_lazy as _

class JenisKelamin(models.TextChoices):
    LAKILAKI = 'L', _('Laki-laki')
    PEREMPUAN = 'P', _('Perempuan')

# Create your models here.
class Siswa(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    jenis_kelamin = models.CharField(
        max_length=1,
        choices=JenisKelamin.choices,
    )
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    nisn = models.CharField(max_length=20)
    # sekolah =

    # default
    # create_by = 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        db_table = "siswa"
        ordering = ["-id"]
        verbose_name_plural = "Siswa"


    
