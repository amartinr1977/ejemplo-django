from django.conf.urls import include, url
#from django.contrib import admin

urlpatterns = [
    url(r'^impresoras/', include('impresoras.urls')),
    #url(r'^admin/', admin.site.urls),
]
