import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    help = 'Импортируйте данные из CSV файла'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name = row[0]
                price = float(row[1])
                image = row[2]
                release_date = row[3]
                lte_exists = row[4].lower() == 'yes'
                phone = Phone(name=name, price=price, image=image, release_date=release_date, lte_exists=lte_exists)
                phone.save()