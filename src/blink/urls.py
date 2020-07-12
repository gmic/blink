"""blink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload
from . import views

app_name = "blink"

urlpatterns = [
    path("", image_upload, name="upload"),

    path("", views.HomeView.as_view(), name='home'),
    path('verbetertekst/', include('bettertexts.urls', namespace="verbetertekst")),
    path("bettertexts/", include("bettertexts.urls", namespace="bettertexts")),
    path("admin/", admin.site.urls),
    path("ratings/", include("star_ratings.urls", namespace="ratings")),
    path("comments/", include("django_comments.urls")),
    path("", include("email_registration.urls")),
    path("robots.txt", views.robots),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







"""blink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "blink"


urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path('verbetertekst/', include('bettertexts.urls', namespace="verbetertekst")),
    path("bettertexts/", include("bettertexts.urls", namespace="bettertexts")),
    path("admin/", admin.site.urls),
    path("ratings/", include("star_ratings.urls", namespace="ratings")),
    path("comments/", include("django_comments.urls")),
    path("", include("email_registration.urls")),
    path("robots.txt", views.robots),
]
