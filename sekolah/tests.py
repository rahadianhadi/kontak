from django.test import TestCase
from .models import Sekolah

class SekolahTestCase(TestCase):
    def setUp(self):
        Sekolah.objects.create(npsn="2026822X", nama="SMKN 1 Cimahi", status="Negeri")
    
    def test_sekolah_cek_nama(self):
        """ Cek nama sekolah """
        smkn1 = Sekolah.objects.get(nama="SMKN 1 Cimahi")
        self.assertEqual(smkn1.nama, "SMKN 1 Cimahi")

