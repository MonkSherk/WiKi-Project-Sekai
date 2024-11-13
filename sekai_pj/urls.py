"""
URL configuration for sekai_pj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.static import serve

from sekai_app import views
from sekai_pj import settings
from django.conf.urls import handler404
handler404 = views.custom_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ProjectSekai/', include('sekai_app.urls')),
    # # 404
    # path('',views.custom_404),
    # re_path(r'^[a-zA-Zа-яА-Я0-9_\-\@\.\+\/]+$', views.custom_404, name='404')

    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


