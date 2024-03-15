from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from .default_data import load_default_data
from django.views.generic import ListView

from .models import Invention
from django.views.generic import DetailView

from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Invention, Category
from .forms import InventionForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomePageView(View):
  template_name = "home.html"
  def get(self, request):
    context = {
      'page_title': 'Home Page for Big Wave Surfing',
      'page_heading':  'Welcome to the 3rd most dangerous sport in the world!',
      'page_content': 'Praia do Norte Lighthouse in Nazaré Portugal, where giant waves are formed due to a submarine canyon called the "Nazaré Canyon".  It is the largest underwater canyon in Europe and is about 230 kilometers (140 miles) long with a depth of approximately 5,000 metres (16,000 ft).',
    }
    return render(request, 'home.html', context)



class AboutView(View):  
  template_name = "about.html"
  def get(self, request):
    context = {
      'page_title': 'About Big Wave Surfing',
      'page_heading':  'Big Wave Surfing in Western Australia',
      'page_content': 'The Right is a big wave surfing spot on the southern coast of Western Australia.  The waves are very dangerous because they break over a shallow reef, creating a large hollow tube that can reach up to 20 feet (6 meters) in height. Watch - https://www.redbull.com/au-en/the-right-like-youve-never-seen-it-before',
    }
    return render(request, 'about.html', context)

class SurfingView(View):
  def get(self, request):
    context = {
      'page_title': 'Big Wave Surfing',
      'page_heading': 'Big Wave Surfing',
      'page_content': 'The first video (https://www.youtube.com/watch?v=CIXbZPHLv2o&feature=youtu.be) is of Sebastian Steudtner, a German surfer, breaking the world record for biggest wave ever ridden with a monstrous 86-footer at Nazare in Portugal (October 2020). The next video (https://www.youtube.com/watch?v=1DJxAYc-5IM) was recently filmed over a 3 day period in Febuary 2024 (Feb. 22, 23, and 24) at Nazaré, Portugal.',
    }
    return render(request, 'bigwavesurfing.html', context)


class LocationView(View):
 def get(self, request):
    context = {
      'page_title': 'Best Locations Worldwide',
      'page_heading': 'BIGGEST WAVES IN THE WORLD',
      'page_content': 'Locations: Praia do Norte / Nazaré, Jaws/Peahi, Shipstern Bluff, Puerto Escondido/Playa Zicatela, Punta de Lobos, Pico Alto, Punta Galea, Dungeons, Nelscott Reef, Killers/Todos Santos, Belharra, Mullaghmore Head, Aileens, Banzai Pipeline, Waimea Bay, Cloudbreak, Cortes Bank, Mavericks, Teahupoo, Ghost Tree/Pescadero Point, Velzyland, Log Cabins, The Wedge, Cow Bombie|Cowaramup Bombora, Cape Fear|Ours, The Right, Pedra Branca, The Cribbar Reef, El Buey, Playa Gris|Roca Puta, Papatowai, Laje da Besta, Laje do Shock, Laje da Avalanche',
  }
   
    return render(request, 'location.html', context)

class WipeoutView(View):
 def get(self, request):
    context = {
      'page_title': 'Wipeouts',
      'page_heading': 'Wipeouts',
      'page_content': '',
    }
    return render(request, 'wipeout.html', context)

class DangerView(View):
  def get(self, request):
      context = {
        'page_title': 'Surfing Dangers',
        'page_heading': 'Surfing Dangers',
        'page_content': '',
      }
      return render(request, 'danger.html', context)


#class from which all class based views inherit
class BaseView(TemplateView):
    default_title = 'My Website'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('title', self.default_title)
        return context


class ClassView(BaseView):
  template_name = 'bootswatch.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'Class-Based View',
          'page_heading': 'Welcome to the Class-Based View',
          'page_content': 'This is the content generated by the class-based view.',
      })
      return context


def function_view(request):
  context = {
      'page_title': 'Function-Based View',
      'page_heading': 'Welcome to the Function-Based View',
      'page_content': 'This is the content generated by the function-based view.',
    }
  return render(request, 'bootswatch.html', context)

class ThemeView(BaseView):
  template_name = 'theme.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Add additional context data if needed
      return context

  def post(self, request, *args, **kwargs):
      theme = request.POST.get('theme')
      response = HttpResponseRedirect(reverse('theme'))
      response.set_cookie('theme', theme)
      return response

# views.py


def load_default_data_view(request):
    load_default_data()  # Call the load_default_data function
    return JsonResponse({'status': 'success'})



class InventionListView(ListView):
    model = Invention
    template_name = 'invention_list.html'
    context_object_name = 'inventions'



class InventionDetailView(DetailView):
    model = Invention
    template_name = 'invention_view.html'
    context_object_name = 'invention'

class InventionCreateView(LoginRequiredMixin,CreateView):
  model = Invention
  form_class = InventionForm
  template_name = 'create_invention.html'
  success_url = reverse_lazy('invention-list')

  
class InventionUpdateView(LoginRequiredMixin,UpdateView):
  model = Invention
  form_class = InventionForm
  template_name = 'update_invention.html'
  success_url = reverse_lazy('invention-list')

class InventionDeleteView(LoginRequiredMixin,DeleteView):
  model = Invention
  success_url = reverse_lazy('invention-list')




