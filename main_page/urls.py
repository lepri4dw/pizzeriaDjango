from django.urls import path

from main_page.views import dishes_list_view, dish_list_detail_view

urlpatterns = [
    path('', dishes_list_view),
    path('dish_list/<int:id>/', dish_list_detail_view),
]
