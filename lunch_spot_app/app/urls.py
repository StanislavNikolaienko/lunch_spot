from django.urls import path
from .views import employee, menu, polls, restaurant

urlpatterns = [
    path("api/restaurant/add_restaurant/", restaurant.add_restaurant, name="add_restaurant"),
    path("api/restaurant/update/<int:pk>/", menu.update_menu, name="update_menu"),
    path("api/restaurant/add_employee/", employee.add_employee, name="add_employee"),
    path("api/restaurant/current_day_menu/", menu.current_day_menu, name="current_day_menu"),
    path("api/restaurant/poll_results/", polls.poll_results, name="poll_results"),
]
