
from django.contrib import admin
from django.urls import path, inlude


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))
]
