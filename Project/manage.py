#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BaseProject.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Production')
    os.environ.setdefault('DJANGO_SECRET_KEY','g(f*1zh-kueu*5)du049+e12&$t*7w8na8u!g5(h(=u8oj=7oj')
    os.environ.setdefault('APPLICATION_HTTP_PORT', '9447')
    os.environ.setdefault('APPLICATION_HTTPS_PORT', '9449')

    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = os.environ['APPLICATION_HTTP_PORT']
    
    from configurations.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
