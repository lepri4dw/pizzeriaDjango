from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import DishListModel, Orders, Slider


def main_list_view(request):
    if request.method == "GET":
        dishes_list = DishListModel.objects.all()
        orders_list = Orders.objects.all()
        slider_list = Slider.objects.all()
        return render(request, template_name='index.html', context={
            'dishes_list': dishes_list,
            'orders_list': orders_list,
            'slider_list': slider_list
        })


def dishes_list_view(request):
    if request.method == 'GET':
        dishes_list = DishListModel.objects.all()
        return render(request, template_name='dishes/dishes.html', context={
            'dishes_list': dishes_list,
        })


def dish_list_detail_view(request, id):
    if request.method == 'GET':
        dish_id = get_object_or_404(DishListModel, id=id)
        return render(request, template_name='dish_detail.html', context={'dish': dish_id})


class SearchView(generic.ListView):
    template_name = 'dishes/dishes.html'
    context_object_name = 'dishes_list'
    paginate_by = 5

    def get_queryset(self):
        return DishListModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('id')
        return context


def about_us_view(request):
    return render(request, template_name='about.html')
