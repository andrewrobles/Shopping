import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from api.service.models import Item

for item in Item.objects.all():
    item.delete()