from django.conf.urls import include, url
from django.contrib import admin
from app.views import save_fibonacci

urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', save_fibonacci),
]