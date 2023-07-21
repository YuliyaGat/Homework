from import_export import resources
from .models import Web_sites

class PersonResource(resources.ModelResource):
    class Meta:
        model = Web_sites