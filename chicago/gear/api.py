from tastypie.resources import ModelResource
from chicago.gear.models import UserAccount, GearItem


# API resource for gear items
class GearItemResource(ModelResource):
    class Meta:
        queryset = GearItem.objects.all()
