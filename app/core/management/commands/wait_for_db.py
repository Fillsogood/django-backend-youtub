from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopq2OpError
from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Wating for db Connection...")
        is_db_connected = None
        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except (Psycopq2OpError, OperationalError):
                self.stdout.write("Connection Trying ...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('PostgreSQL Connection Success'))
