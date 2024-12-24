from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView



class Homepage(TemplateView):
    template_name = "homepage.html"



class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list --- lista de itens do modelo

class DetalhesFilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object --- 1 item do modelo

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:3]
        context["filmes_relacionados"] = filmes_relacionados
        return context



# def homefilmes(request):
#    context = {}
#    lista_filmes = Filme.objects.all()
#   context ['lista_filmes'] = lista_filmes
#   return render(request, "homefilmes.html", context)


# Create your views here.
#def homepage(request):
#    return render(request, "homepage.html")