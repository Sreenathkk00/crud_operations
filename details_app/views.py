from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView
from django.views import generic
from .models import DetailsModel
from .forms import DetailForm
# Create your views here.

# list the details 
class DetailListview(ListView):
    model = DetailsModel
    queryset = DetailsModel.objects.filter().all().order_by('-pub_date') 
        
    template_name = 'index.html'
    context_object_name = 'Details_List'
    

# creat the details
class FormView(CreateView):
    model = DetailsModel
    form_class = DetailForm
    template_name = 'form.html'
    success_url ='/' 

# update the details
class UpdateView(UpdateView):
    model = DetailsModel
    

print(dir(generic))