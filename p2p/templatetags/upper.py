__author__ = 'root'
from django import template

register = template.Library()


class UpperNode(template.Node):
    def __init__(self,nodelist):
        self.nodelist = nodelist

    def render(self, context):
        content = self.nodelist.render(context)
        return context.upper()


@register.tag
def upper(parser,token):
    nodelist = parser.parse("endupper")
    parser.delete_first_token()
    return UpperNode(nodelist)
