from django.contrib import admin
from django.urls import path, include
from todo import urls as todos_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="STHIMA's ToDos API Documentation")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(todos_urls, namespace='todos')),
    path('swagger/', schema_view)
]
