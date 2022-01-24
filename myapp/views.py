from django.shortcuts import render
from django.http import HttpResponse
from .models      import gmodel
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from .forms import gforms

def hello(request):
    text="""<h1>welcome to my app !</h1>"""
    return HttpResponse(text)
# Create your views here.

def l_view(request):
    context={}
    context["d"]=gmodel.objects.all()
    return render(request,"l_view.html",context)

class glist(ListView):
    model=gmodel

class gcreate(CreateView):
    model=gmodel
    fields =["title","des"]
    success_url = "/"


class gupdate(UpdateView):
    model=gmodel
    fields =["title","des"]

    success_url = "/"


class gdelete(DeleteView):
    model=gmodel
    success_url = "/"

class gformsview(FormView):
    form_class = gforms
    template_name = "myapp/gforms.html"
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
