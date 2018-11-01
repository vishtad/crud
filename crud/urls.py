"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from employee import views  
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [  
	path('admin/', admin.site.urls),  
	path('emp', views.emp),  
	path('show',views.show),  
	path('edit/<int:id>', views.edit),  
	path('update/<int:id>', views.update),  
	path('delete/<int:id>', views.destroy),  
	path('',views.home),
	path('rr',views.registration),
	path('login',views.login),
	path('check',views.check),
	path('logout',views.log_out),
	#path('search',views.search),
	path('search',views.search1),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 