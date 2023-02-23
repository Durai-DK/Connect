from .serializers import *
from rest_framework import generics

class Showroomlist(generics.ListAPIView):
    queryset = Showroom_Details.objects.all()
    serializer_class = Showroom_Serializer


class Outletlist(generics.ListAPIView):

    queryset = Outlet_Media.objects.all()
    serializer_class = Outlet_Media