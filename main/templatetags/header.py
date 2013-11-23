from django import template
from main.models import *

register = template.Library()

class RootCategoriesNode(template.Node):
    def render(self, context):
        context['root_categories'] = Category.objects.filter(parent=None)
        return ''

@register.tag
def get_root_categories(parser, token):
    return RootCategoriesNode()