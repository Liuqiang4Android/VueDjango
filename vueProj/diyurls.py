
from django.contrib import admin
from django.views.generic import TemplateView
import VueDjango.urls
from django.urls import path,include

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^api/', include(VueDjango.urls)),
    path(r'^$', TemplateView.as_view(template_name="index.html")),
]