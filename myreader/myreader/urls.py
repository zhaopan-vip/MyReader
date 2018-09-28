"""myreader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from mainsite import views

urlpatterns = [
    path('', views.homepage),
    path('book/<int:bookid>', views.book),
    path('book/<int:bookid>/<int:section>', views.book_section),
    path('book_manager/', views.book_manager),
    path('book_manager/<int:sourceid>', views.book_manager_source),
    path('book_manager/<int:sourceid>/<int:section>', views.book_manager_source_section),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)