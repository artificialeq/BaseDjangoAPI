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
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request_data = request.data

        user = User(
            name=[request_data["name"]],
            birth_date = [request_data["birth_date"]],
            profile_picture = [request_data["profile_picture"]],
            about_me = [request_data["about"]],
            status = [request_data["status"]]
        )

        user.save()
