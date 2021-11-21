from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Women

# menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

menu = [{'title': "О сайте", 'url_name': "about"},
        {'title': "Добавить статью", 'url_name': "add_page"},
        {'title': "Обратная связь", 'url_name': "contract"},
        {'title': "Войти", 'url_name': "login"}]


# Create your views here.
def index(request):  # HttpRequest
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html',  context=context)


def about(request):
    posts = Women.objects.all()
    return render(request, 'women/about.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def add_page(request):

    return HttpResponse('Добавление статьи')


def contract(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1> {exception}')


def show_post(request, post_id):
    return HttpResponseNotFound(f'Отображение статьи с id = {post_id}')

#
#
# def categories(request):
#     return HttpResponse("<h1>Статьи по категорям</h1>")
#
#
# def categories2(request, catid):
#     if request.GET:
#         print(request.GET)
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f"<h1>Статьи по категорям</h1><p>{catid}</p>")
#
#
# def categories3(request, cat):
#     return HttpResponse(f"<h1>Статьи по категорям</h1><p>{cat}</p>")
#
#
# def archive(request, year, month):
#     if int(year) > 2020:
#         raise Http404()
#     if int(month) > 20:
#         #return redirect('/', permanent=True)
#         return redirect('home', permanent=True)
#
#     return HttpResponse(f"<h1>Архив по годам</h1><p>{year}-{month}</p>")


