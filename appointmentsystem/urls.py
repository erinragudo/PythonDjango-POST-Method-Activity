from django.contrib import admin
from django.urls import path
from django.urls import include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scheduling.urls')),
    path('appointments/', include('scheduling.urls')),
    # path('', lambda request: HttpResponseRedirect('/appointments/create/')),
]
