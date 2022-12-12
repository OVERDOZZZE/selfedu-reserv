from django import template
from main_app.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('main_app/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}

