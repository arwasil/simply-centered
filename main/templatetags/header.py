from django import template
from main.models import *

register = template.Library()

class RootCategoriesNode(template.Node):
    def render(self, context):
        context['root_menu'] = Category.objects.filter(show_in_menu=True, parent=None)
        return ''

@register.tag
def get_root_categories(parser, token):
    return RootCategoriesNode()