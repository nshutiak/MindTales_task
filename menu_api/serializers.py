from rest_framework import serializers
from .models import Employee, Menu, Restaurant, VoteMenu

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = '__all__'

    def get_restaurant_name(self, obj):
        return obj.restaurant.name

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class VoteMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteMenu
        fields = '__all__'