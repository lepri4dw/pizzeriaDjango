from django.urls import path

from main_page.views import main_list_view, dishes_list_view, dish_list_detail_view, SearchView, about_us_view

urlpatterns = [
    path('', main_list_view, name='home'),
    path('about/', about_us_view, name='about'),
    path('dishes/', dishes_list_view, name='dishes'),
    path('dish_list/<int:id>/', dish_list_detail_view),
    path('search/', SearchView.as_view(), name='search')
]
