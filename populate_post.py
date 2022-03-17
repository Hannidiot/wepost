import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_projects.settings')

import django
django.setup()
from wepost_main.models import *

def populate():
    pass
