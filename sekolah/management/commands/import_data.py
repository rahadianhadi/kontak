import csv

from django.core.management import BaseCommand
from django.utils import timezone


from sekolah.models import Sekolah

class Command(BaseCommand):
    help = "Import data sekolah dari CSV"

    def add_arguments(self, parser):
        parser.add_argument("filepath", type=str)
    
    def handle(self, *args, **options):
        ''' Import function  '''
        start_time = timezone.now()
        filepath = options["filepath"]

        # print(f"File: {filepath}")

        # Baca csv
        with open(filepath, "r") as csv_file:
            data_csv = csv.reader(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)

            count = 0
            fields = []
            data_bulk = []

            for row in data_csv:
                
                if count == 0:
                    fields = row
                else:
                    self.row_save(fields, row, Sekolah())
                count += 1
        
        # Tampilkan hasil
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
    
    def row_save(self, fields, row, model):
        
        count_field = 0
        for field in fields:
            # print(f'Fields name {field}')
            model.__dict__[field] = (row[count_field].strip())
            count_field += 1
        try:
            print("Save record")
            model.save()
        except Exception as e:
            print(e)
    