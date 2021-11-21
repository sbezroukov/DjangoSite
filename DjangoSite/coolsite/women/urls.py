from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('addpage/', add_page, name='add_page'),
    path('contract/', contract, name='contract'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post')
    # path('cats/', categories),  # http://127.0.0.1:8000/cats2/
    # path('cats2/<int:catid>/', categories2),  # http://127.0.0.1:8000/cats2/1/
    # path('cats2/<slug:cat>/', categories3),  # http://127.0.0.1:8000/cats2/1/
    # re_path(r'archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', archive),  # http://127.0.0.1:8000/cats2/1/
]
