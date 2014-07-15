from hedonometer.models import Event,Book,Happs
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields

class FixedFloatField(fields.ApiField):
    """
    A field for return fixed-width floats.
    """
    dehydrated_type = 'string'
    help_text = 'Fixed precision numeric data. Ex: 26.73'

    def convert(self, value):
        if value is None:
            return None

        if value and not isinstance(value, basestring):
            value = '{0:.3f}'.format(value)

        return value

    def hydrate(self, bundle):
        value = super(FixedFloatField, self).hydrate(bundle)

        if value and not isinstance(value, basestring):
            value = '{0:.3f}'.format(value)

        return value

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        limit = 500
        filtering = {
            'importance': ALL,
        }

class HappsResource(ModelResource):
    happiness = FixedFloatField(attribute='value')
    class Meta:
        queryset = Happs.objects.all()
        excludes = ['value','id',]
        resource_name = 'timeseries'
        limit = 3000
        # default_format = ['json']
        max_limit = None
        include_resource_uri = False
        filtering = {
            'date': ALL,
        }

class BookResource(ModelResource):
    happiness = FixedFloatField(attribute='happs')
    reference = fields.CharField('filename')
    class Meta:
        queryset = Book.objects.filter(length__gte=10000)
        resource_name = 'gutenberg'
        excludes = ['happs','id','filename',]
        include_resource_uri = False
        max_limit = None
        limit = 500
        filtering = {
            'title': ALL_WITH_RELATIONS,
            'id': ALL,
        }

class RandomBookResource(ModelResource):
    reference = fields.CharField('filename')
    class Meta:
        queryset = Book.objects.filter(length__gte=10000).order_by('?')
        resource_name = 'randombook'
        limit = 1











