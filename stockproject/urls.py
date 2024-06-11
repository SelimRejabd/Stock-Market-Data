from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('stockdata.urls')),
    path('api/stocks-data/', include('stock_database.urls'))
]
