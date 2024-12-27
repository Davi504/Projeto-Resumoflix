from django.shortcuts import render, redirect, reverse 
from .models import Filme
from .forms import CriarContaForm
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin



class Homepage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("filme:homefilmes")
        else:
            return super().get(request, *args, **kwargs) #redirecionando pra homepage

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list --- lista de itens do modelo

class DetalhesFilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object --- 1 item do modelo

    def get(self, request, *args, **kwargs):
        # Incrementar o número de visualizações
        Filme = self.get_object()
        Filme.visualizacoes += 1
        Filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(Filme)
        
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:3]
        context["filmes_relacionados"] = filmes_relacionados
        return context
    
class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get("query")
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None
    

class PaginaPerfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"


class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("filme:login")

# def homefilmes(request):
#    context = {}
#    lista_filmes = Filme.objects.all()
#   context ['lista_filmes'] = lista_filmes
#   return render(request, "homefilmes.html", context)


# Create your views here.
#def homepage(request):
#    return render(request, "homepage.html")