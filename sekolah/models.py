from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class StatusSekolah(models.TextChoices):
    SWASTA = 'Swasta', _('Swasta')
    NEGERI = 'Negeri', _('Negeri')

# Create your models here.
class Sekolah(models.Model):
    npsn = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    provinsi = models.CharField(blank=True, null=True, max_length=50)
    kabupaten_kota = models.CharField(blank=True, null=True, max_length=50)
    kecamatan = models.CharField(blank=True, null=True, max_length=50)
    status = models.CharField(
        max_length=10,
        choices=StatusSekolah.choices,
    )

    # default
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="sekolah_created_by")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        db_table = "sekolah"
        ordering = ["-id"]
        verbose_name_plural = "Sekolah"


    
