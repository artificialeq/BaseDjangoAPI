import requests
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from api.models import User
from api.serializers import UserSerializer

def home(request):
    return HttpResponse("Hello, Django!")

class UserViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    parser_classes = (MultiPartParser, FormParser)
    queryset = User.objects.all()
    serializer_class = UserSerializer
