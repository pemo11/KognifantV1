from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Der + static Zusatz sollte nicht im Productionsystem enthalten sein!
# Ich habe es also noch nicht verstanden (bzw. wusste es einmal)
# aber nur so geht es!
# https://docs.djangoproject.com/en/4.2/howto/static-files/