from django import template
from ..models import MenuItem
register = template.Library()


@register.inclusion_tag("menu/generate_menu.html")
def get_menu():
    items = MenuItem.objects.all()
    return {'items': items}


@register.inclusion_tag("menu/generate_phone_menu.html")
def get_phone_menu():
    items = MenuItem.objects.all()
    return {'items': items}
