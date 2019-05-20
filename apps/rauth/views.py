# REST framework
from rest_framework import renderers
from rest_framework.authtoken.views import ObtainAuthToken


class AuthUserView(ObtainAuthToken):
    renderer_classes = (renderers.JSONRenderer, renderers.AdminRenderer)
