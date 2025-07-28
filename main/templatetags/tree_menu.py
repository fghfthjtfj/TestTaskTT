from django import template
from django.urls import reverse, NoReverseMatch, resolve
from main.models import *

register = template.Library()


@register.inclusion_tag('main/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):

    request = context['request']
    path = request.path

    items = list(MenuItem.objects.filter(menu__title=menu_name).order_by('order'))
    if not items:
        return {'menu_items': [], 'request': request}

    id_to_item = {item.id: item for item in items}
    tree = []
    for item in items:
        item.children_list = []
    for item in items:
        if item.parent_id:
            id_to_item[item.parent_id].children_list.append(item)
        else:
            tree.append(item)

    def mark_open(item):  # Рекурсивно помечаем родительские элементы как "открытые"
        item.is_open = True
        if item.parent_id:
            mark_open(id_to_item[item.parent_id])

    for item in items:
        url = item.url
        try:
            resolved_url = reverse(url) if item.named_url else url
        except NoReverseMatch:
            resolved_url = url

        item.resolved_url = resolved_url
        if resolved_url == path:
            mark_open(item)

    return {'menu_items': tree, 'request': request}

