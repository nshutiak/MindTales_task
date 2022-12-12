from django.urls import path
from .views import ClearvotesAPIView, EmployeeCreateView, MenuDestroyAPIView, MenuListCreateAPIView, RestaurantListCreateAPIView, VoteMenuCreateAPIView, MenuofthedayAPIView

urlpatterns = [
    path('restaurant/', RestaurantListCreateAPIView.as_view()),
    path('menu/', MenuListCreateAPIView.as_view()),
    path('menu/<int:pk>/', MenuDestroyAPIView.as_view()),
    path('employee/', EmployeeCreateView.as_view()),
    path('menu/vote/', VoteMenuCreateAPIView.as_view()),
    path('menu_of_day/', MenuofthedayAPIView.as_view()),
    path('clear_vote_result/', ClearvotesAPIView.as_view())
]