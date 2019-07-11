from django.urls import path

import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.home),
    path('contact', views.contact_me),
    path('projects', views.projects),
    path('blog', views.blog),
    path('/send-email', views.send_email),

]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

