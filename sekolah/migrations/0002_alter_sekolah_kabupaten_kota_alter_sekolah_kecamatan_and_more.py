# Generated by Django 4.1.5 on 2023-01-18 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sekolah", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sekolah",
            name="kabupaten_kota",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="sekolah",
            name="kecamatan",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="sekolah",
            name="provinsi",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
