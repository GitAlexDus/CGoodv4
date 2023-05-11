
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
#from django.views import View
#from django.db import transaction

from .models import Resa, Casier, Placard
from .forms import ResaForm, Pincheck

import paho.mqtt.publish as pub #import the publisher de paho

# Create your views here.

# Login and registartion views

class CustomLoginView(LoginView):
    template_name = 'booking/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('resas')


class RegisterPage(FormView):
    template_name = 'booking/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('resas')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('resas')
        return super(RegisterPage, self).get(*args, **kwargs)

# Resa list, creation, update, and delet

class ResaList(LoginRequiredMixin, ListView):
    model = Resa
    context_object_name = 'resas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resas'] = context['resas'].filter(user=self.request.user)
        return context


class ResaUpdate(LoginRequiredMixin, UpdateView):
    model = Resa
    fields = ["ResDate", "ResHeure", "ResNbreHeure" , "ResPIN" ]
    success_url = reverse_lazy('resas')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Resa
    context_object_name = 'resa'
    success_url = reverse_lazy('resas')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class ResaPlacard(LoginRequiredMixin, ListView):
    model = Placard
    context_object_name = 'placards'
    success_url ='resa-select-objet'
    paginate_by = 10

def SelectCasier(request, Placard_id):
    CasiersDuPlacard= Casier.objects.filter(placard=Placard_id)
    template = loader.get_template("Booking/casier_list.html")
    context = {
        "casiers": CasiersDuPlacard,
    }
    return HttpResponse(template.render(context, request))


def ResaFinish(request, Casier_id):
    # if this is a POST request we need to process the form data
    if request.method == "POST":


        # create a form instance and populate it with data from the request:
        form = ResaForm(request.POST)
        
        if form.is_valid():
            casierid=Casier_id
            date=form.cleaned_data['your_Date']
            heure=form.cleaned_data['your_time']
            nbreheure=form.cleaned_data['your_NbreHeure']
            pin=form.cleaned_data['your_Pin']
            f = Resa (user=request.user, casier_id=casierid, ResDate= date, ResHeure= heure, ResNbreHeure= nbreheure, ResPIN=pin)
            f.save()
            return HttpResponseRedirect(reverse("resas"))

            
        else:
            print (f)
            return HttpResponse("ca marche pas")
    else:
        form = ResaForm()

    return render(request, "Booking/resaform.html", {"form": form})


# Ouverture des casier

def get_Pin(request, Casier_id):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Pincheck(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pin=form.cleaned_data['your_Pin']
            resa = Resa.objects.filter(casier=Casier_id)
            codePin =', '.join([q.ResPIN for q in resa ])
            if pin == codePin :
                cas = Casier.objects.filter(id=Casier_id)
                code = b'\x8a\x01\x03\x11\x99' #Trouver une solution pour stocker de l hex dans la base pour l instant envisager une de stocker les codes dans le code. 
                topic= ', '.join([q.CasMqttTopic for q in cas])
                numero = [q.CasNum for q in cas ]
                date_heure = ([q.ResDate for q in resa ])
                nbre_heure = ([q.ResNbreHeure for q in resa ])
                pub.single(topic, code, hostname="91.121.93.94", port=1883)
                return HttpResponse("Loker open :Casier %(w)s referance  %(x)s Message %(y)s Topic: %(z)s. PIN %(zz)s Date %(zzz)s Duree %(zzzz)s"
                 % {'w':numero, 'x':Casier_id, 'y':code, 'z':topic, 'zz': codePin, 'zzz': date_heure, 'zzzz': nbre_heure })

            
            else:
                return HttpResponse("Wrong Pin or No Booking")
    else:
        form = Pincheck()

    return render(request, "Booking/open.html", {"form": form})

