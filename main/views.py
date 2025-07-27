from django.urls import resolve
from django.http import Http404
from django.shortcuts import render

page_titles = {
    'home': 'Главная',
    'about': 'О нас',
    'catalog': 'Каталог',
    'contacts': 'Контакты',
    'team': 'Команда',
    'team_about_team': 'Команда о команде',
    'offices': 'Офисы',
}


def static_page(request):
    url_name = resolve(request.path).url_name
    if url_name not in page_titles:
        raise Http404
    return render(request, 'main/home.html', {'title': page_titles[url_name]})
