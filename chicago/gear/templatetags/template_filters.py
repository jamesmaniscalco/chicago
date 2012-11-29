# template filters for Gear app

from django import template

register = template.Library()


# return the weight of a gear item in the user's preferred units
@register.filter
def gear_item_weight(gear_item, user):
    return gear_item.get_weight(user)
