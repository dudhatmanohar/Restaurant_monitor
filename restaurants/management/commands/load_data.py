# restaurants/management/commands/load_data.py

import csv
from datetime import datetime
import pytz
from django.core.management.base import BaseCommand
from django.db import models
from restaurants.models import StoreStatus
from restaurants.models import BusinessHours
from restaurants.models import StoreTimezone






class Command(BaseCommand):
    help = 'Load data from CSV files'

    def handle(self, *args, **kwargs):
        utc = pytz.UTC  # Define UTC timezone
        with open(r'C:\Users\dell\monitor\store.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # Correctly parse the timestamp with fractional seconds and timezone
                    timestamp_utc = datetime.strptime(row['timestamp_utc'], '%Y-%m-%d %H:%M:%S.%f %Z')
                    # Convert to timezone-aware datetime
                    timestamp_utc = utc.localize(timestamp_utc)
                except ValueError as e:
                    self.stdout.write(self.style.ERROR(f"Error parsing date: {e}"))
                    continue

                StoreStatus.objects.create(
                    store_id=row['store_id'],
                    status=row['status'],
                    timestamp_utc=timestamp_utc
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data into StoreStatus'))



        # Load Business Hours
        with open(r'C:\Users\dell\monitor\menu.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                BusinessHours.objects.create(store_id=row[0], day_of_week=row[1], start_time_local=row[2], end_time_local=row[3])

        # Load Timezone
        with open(r'C:\Users\dell\monitor\V3.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                StoreTimezone.objects.create(store_id=row[0], timezone_str=row[1])
