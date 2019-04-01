# api/resources.py

from tastypie.resources import ModelResource
from api.models import Note

class NoteResources(ModelResource):
  class Meta:
    queryset = Note.objects.all()
    resource_name = 'note'
