"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.urls import path, include

from coolsite import settings
from women.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),  # http://127.0.0.1:8000/women/
    # path('cats/', categories),  # http://127.0.0.1:8000/cats/
    # path('women/', include('women.urls'))
    path('', include('women.urls')),
]

# В режиме дебаг для статических данных и графических файлов
# Добавляем ещё 1 путь
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# settings.MEDIA_URL - префикс
# settings.MEDIA_ROOT - корневая папка
# На реальных серверах это уже настроено, поэтому на локальном прописываем вручную

handler404 = pageNotFound
