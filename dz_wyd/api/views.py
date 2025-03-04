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

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import requests
from bs4 import BeautifulSoup

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import requests
from bs4 import BeautifulSoup


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def search_fact(request):
    query = request.GET.get('query')
    if not query:
        return Response({"error": "Please provide a 'query' parameter."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Perform a search on DuckDuckGo
        url = f"https://duckduckgo.com/html/?q={query}+answer+as+in+2025"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract snippet (answer) from search results
            snippets = soup.find_all('a', class_='result__snippet', limit=1)
            if snippets:
                answer = snippets[0].text.strip()
                return Response({
                    "query": query,
                    "answer": answer
                })
            else:
                return Response({"message": "No answer found for your query."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Failed to fetch search results."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)