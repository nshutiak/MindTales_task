from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Employee, Restaurant, Menu, VoteMenu
from .serializers import EmployeeSerializer, RestaurantSerializer, MenuSerializer, VoteMenuSerializer
from rest_framework import status
from rest_framework.response import Response

class MenuListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MenuSerializer
    
    def get_queryset(self):
        Day = self.request.query_params.get("day")
        menu_of_day = Menu.objects.filter(day_of_week= Day)
        return menu_of_day

class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer

class MenuDestroyAPIView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    permission_classes = (IsAuthenticated,)

class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class VoteMenuCreateAPIView(generics.CreateAPIView):
    serializer_class = VoteMenuSerializer
    permission_classes = (IsAuthenticated,)

class MenuofthedayAPIView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        day = self.request.query_params.get("day")
        menu_objs = Menu.objects.filter(day_of_week=day)
        voted_count = {}
        for obj in menu_objs:
            count = len(VoteMenu.objects.filter(menu_id=obj.id))
            voted_count[obj.content]=count
        max_menu_vote_id = max(voted_count, key=voted_count.get)
        if voted_count[max_menu_vote_id] == 0:
            return Response("No votes found", status=status.HTTP_200_OK)
        menu = Menu.objects.filter(content=max_menu_vote_id)
        serializer = MenuSerializer(data=menu, many=True)
        serializer.is_valid()
        return Response({   'menu': serializer.data,
                            'votes': voted_count}, status=status.HTTP_200_OK)

class ClearvotesAPIView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        VoteMenu.objects.all().delete()
        return Response('all votes were deleted',status=status.HTTP_200_OK)

