"""p2p URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from p2p.apps.home.upload import upload_image
admin.autodiscover()

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^home/',include('p2p.apps.home.urls')),
    url(r'^index/',include('p2p.apps.index.urls')),
    url(r"^uploads/(?P<path>.*)$", \
                "django.views.static.serve", \
                {"document_root": settings.MEDIA_ROOT,}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', 'p2p.apps.index.views.index'),
]
