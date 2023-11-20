from django.shortcuts import render, get_object_or_404
from .models import DishListModel, Orders, Slider

def dishes_list_view(request):
    if request.method == "GET":
        dishes_list = DishListModel.objects.all()
        orders_list = Orders.objects.all()
        slider_list = Slider.objects.all()
        return render(request, template_name='index.html', context={
            'dishes_list': dishes_list,
            'orders_list': orders_list,
            'slider_list': slider_list
        })
def dish_list_detail_view(request, id):
    if request.method == 'GET':
        dish_id = get_object_or_404(DishListModel, id=id)
        return render(request, template_name='dish_detail.html', context={'dish': dish_id})
