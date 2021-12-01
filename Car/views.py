from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Car
from .serializers import CarSerlizer
from .permissions import IsAuthorOrReadOnly

class CarList(ListCreateAPIView):
   
    permission_classes = (IsAuthenticatedOrReadOnly,)
   
    queryset = Car.objects.all()
   
    serializer_class = CarSerlizer

class CarDetail(RetrieveUpdateDestroyAPIView):
   
    permission_classes = (IsAuthorOrReadOnly,)
   
    queryset = Car.objects.all()
   
    serializer_class = CarSerlizer