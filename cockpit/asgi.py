import os 

from django.core.asgi import get_asgi_application
from django.urls import path
from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from cockpit.routing import application as websocket_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cockpit.settings')

application = get_asgi_application()
