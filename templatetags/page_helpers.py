from mezzanine.pages.models import Page

from mezzanine import template

register = template.Library()


@register.as_tag
def page_by_slug(slug):
    """
    Return a page matching the provided slug, eg 'index' or 'about/team'
    """
    try:
        return Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        return None


@register.as_tag
def page_by_id(id):
    """
    Return a page by id
    """
    try:
        return Page.objects.get(pk=id)
    except Page.DoesNotExist:
        return None
