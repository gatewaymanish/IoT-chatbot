from django.conf.urls import include, url
from .views import ManixBot

urlpatterns = [
    url(r'^474f74d21ecf61b2621ead4ecfaa9e39d36008f037728489b8/?$', ManixBot.as_view())
]
