#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from multiprocessing import Process
from consumer import connectConsumer

def run_consumer():
    connectConsumer()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Twiddit_profile_ms.settings')
    try:
        # Iniciar el consumidor
        consumer_process = Process(target=run_consumer)
        consumer_process.start()
        # Iniciar el servidor de Django 
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
