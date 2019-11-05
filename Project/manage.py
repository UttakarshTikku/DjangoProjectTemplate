#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import dotenv


def main():
    dotenv.read_dotenv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BaseProject.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Production')
    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = os.environ['APPLICATION_PORT']
    
    from configurations.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
