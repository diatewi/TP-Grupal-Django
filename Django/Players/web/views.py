from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Groups, FreePlayers
from django.urls import reverse, reverse_lazy

def index(request):
    return render(request, 'web/index.html')

def login(request):
    return render(request, 'web/login.html')

def signup(request):
    return render(request, 'web/signup.html')

def contact(request):
    return render(request, 'web/contact.html')


# def leagueoflegends_groups(request):
    
    # posible_servers = ['LAS', 'BR', 'NA', 'LAN', 'EUW', 'KR', 'EUNE', 'OCE', 'TR', 'RU', 'JP']
    # posible_gamemodes = ['Partida rapida', 'Reclutamiento', 'Clasificatoria duo', 'Flexible', 'ARAM', 'TFT', 'Arena']
#     groups = Groups.objects.all()

#     return render(request, 'web/games/league of legends/lol-groups.html', {'groups': groups, 'posible_servers': posible_servers, 'posible_gamemodes': posible_gamemodes})

class GroupsListView(ListView):
    model = Groups
    context_object_name = 'groups'


    def get_template_names(self):
        game = self.kwargs.get('game', 'default_game')
        return ['web/games/{}/groups.html'.format(game)]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.kwargs.get('game', 'default_game')

        if game == 'League-of-legends':
            context['posible_servers'] = ['LAS', 'BR', 'NA', 'LAN', 'EUW', 'KR', 'EUNE', 'OCE', 'TR', 'RU', 'JP']
            context['posible_gamemodes'] = ['Partida rapida', 'Reclutamiento', 'Clasificatoria duo', 'Flexible', 'ARAM', 'TFT', 'Arena']
        return context

class PlayersListView(ListView):
    model = FreePlayers
    context_object_name = 'freePlayers'

    def get_template_names(self):
        game = self.kwargs.get('game', 'default_game')
        return ['web/games/{}/players.html'.format(game)]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.kwargs.get('game', 'default_game')
       
        if game == 'League-of-legends':
            context['posible_servers'] = ['LAS', 'BR', 'NA', 'LAN', 'EUW', 'KR', 'EUNE', 'OCE', 'TR', 'RU', 'JP']
            context['posible_gamemodes'] = ['Partida rapida', 'Reclutamiento', 'Clasificatoria duo', 'Flexible', 'ARAM', 'TFT', 'Arena']
        return context

    
class GroupsCreateView(CreateView):
    model = Groups
    template_name = 'web/create_group.html'
    fields = '__all__'
    success_url = 'groups/League-of-legends'


class GroupsUpdateView(UpdateView):
    model = Groups
    template_name = 'web/update_group.html'
    fields = '__all__'
    success_url = '../groups/League-of-legends'

class GroupsDeleteView(DeleteView):
    model = Groups
    template_name = 'web/delete_group.html'
    game = 'League-of-legends'
    
    def get_success_url(self):
        return reverse_lazy('groups_list', kwargs={'game': self.game})