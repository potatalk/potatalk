"""
URL configuration for potatalkLLMProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from main.views import MainView
from kyusanLLM.views import InformationView, MessageView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('kyusanLLM/', include('kyusanLLM.urls')),
    path('jooLLM/', include('jooLLM.urls')),
    path('songLLM/', include('songLLM.urls')),
    path('kangLLM/', include('kangLLM.urls')),
    path('kyuilLLM/', include('kyuilLLM.urls')),
    # path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)