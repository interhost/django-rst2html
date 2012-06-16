"""
"""

from django import template
from django.contrib.markup.templatetags.markup import restructuredtext

register = template.Library()

@register.tag
def rst2html(parser, token):
    nodelist = parser.parse(('endrst2html',))
    parser.delete_first_token()
    return RSTNode(nodelist)

class RSTNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        rst = self.nodelist.render(context)
        return restructuredtext(rst)
