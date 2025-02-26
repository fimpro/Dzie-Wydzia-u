from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
import datetime
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def api_home(request):
    return Response({"message": "Welcome to the API!"})

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_tasks(request):
    tasks = [{"id": 1, "name": "Task 1"}, {"id": 2, "name": "Task 2"}]
    return Response(tasks)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
def create_task(request):
    return Response({"message": "Task created successfully!"})

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_date(request):
    print(datetime.date.today())
    return Response([datetime.datetime.now().strftime("%B %d, %Y %H:%M")])

from rest_framework import generics
from main.models import User
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer