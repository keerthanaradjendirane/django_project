from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListCreate(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
