"""challenge URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from rest_framework_nested import routers
from schools import views as school_views


router = routers.SimpleRouter()
router.register(r'schools', school_views.SchoolViewSet)
router.register(r'students', school_views.StudentViewSet)

school_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
school_router.register(r'students', school_views.StudentViewSet, base_name="student")


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(school_router.urls)),
    path('admin/', admin.site.urls),
]
