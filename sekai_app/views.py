from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from sekai_pj.settings import SECRET_WORD, ADMIN_TOKEN
from .decorators import admin_token_required
from .forms import EventForm, SongForm, CardForm, CharacterForm, GroupForm, SekaiWorldForm, SekaiItemsForm
from .models import SekaiWorld, Group, Character, Card, Song, Event, GameStuff, SekaiItems


def home(request):
    popular_characters = Character.objects.filter(is_popular=True)
    active_events = Event.objects.filter(is_ended=False)
    game_stuff = GameStuff.objects.all()
    return render(request, 'sekai_app/home.html', {
        'popular_characters': popular_characters,
        'active_events': active_events,
        'games':game_stuff
    })



# SEKAI Worlds
class SekaiWorldListView(ListView):
    model = SekaiWorld
    template_name = 'sekai_app/sekai_worlds.html'
    context_object_name = 'sekai_worlds'

    def get_queryset(self):
        queryset = SekaiWorld.objects.all()
        query = self.request.GET.get('query')
        group_filter = self.request.GET.get('group')

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if group_filter:
            queryset = queryset.filter(groups__name__icontains=group_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

class SekaiWorldDetailView(DetailView):
    model = SekaiWorld
    template_name = 'sekai_app/sekai_world_detail.html'
    context_object_name = 'sekai_world'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sekai_items'] = self.object.get_items()
        return context

# Group Views
class GroupListView(ListView):
    model = Group
    template_name = 'sekai_app/groups.html'
    context_object_name = 'groups'

    def get_queryset(self):
        queryset = Group.objects.all()
        query = self.request.GET.get('query')
        sekai_filter = self.request.GET.get('sekai')

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if sekai_filter:
            queryset = queryset.filter(sekai__name__icontains=sekai_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sekai_worlds'] = SekaiWorld.objects.all()
        return context


class GroupDetailView(DetailView):
    model = Group
    template_name = 'sekai_app/group_detail.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.get_object()

        context['songs'] = group.get_songs()
        context['characters'] = group.get_characters()

        return context

# Character Views
class CharacterListView(ListView):
    model = Character
    template_name = 'sekai_app/characters.html'
    context_object_name = 'characters'

    def get_queryset(self):
        queryset = Character.objects.all()
        query = self.request.GET.get('query')
        group_filter = self.request.GET.get('group')
        type_filter = self.request.GET.get('type')

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if group_filter:
            queryset = queryset.filter(group__name__icontains=group_filter)

        if type_filter:
            queryset = queryset.filter(sekai_type=type_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


# views.py

class CharacterDetailView(DetailView):
    model = Character
    template_name = 'sekai_app/character_detail.html'
    context_object_name = 'character'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character = self.get_object()

        context['songs'] = character.get_songs()
        context['cards'] = character.cards.all()

        return context


# Card Views
class CardListView(ListView):
    model = Card
    template_name = 'sekai_app/cards.html'
    context_object_name = 'cards'

    def get_queryset(self):
        queryset = Card.objects.all()
        query = self.request.GET.get('query')
        rarity_filter = self.request.GET.get('rarity')
        character_filter = self.request.GET.get('character')

        if query:
            queryset = queryset.filter(Q(character__name__icontains=query) | Q(stats__icontains=query))

        if rarity_filter:
            queryset = queryset.filter(rarity=rarity_filter)

        if character_filter:
            queryset = queryset.filter(character__name__icontains=character_filter)

        return queryset


class CardDetailView(DetailView):
    model = Card
    template_name = 'sekai_app/card_detail.html'
    context_object_name = 'card'

# Song Views
class SongListView(ListView):
    model = Song
    template_name = 'sekai_app/songs.html'
    context_object_name = 'songs'

    def get_queryset(self):
        queryset = Song.objects.all()
        query = self.request.GET.get('query')
        artist_filter = self.request.GET.get('artist')
        genre_filter = self.request.GET.get('genre')

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(artist__name__icontains=query) | Q(genre__icontains=query)
            )

        if artist_filter:
            queryset = queryset.filter(artist__name__icontains=artist_filter)

        if genre_filter:
            queryset = queryset.filter(genre__iexact=genre_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Song.GENRE_CHOICES
        return context

class SongDetailView(DetailView):
    model = Song
    template_name = 'sekai_app/song_detail.html'
    context_object_name = 'song'

# Event Views
class EventListView(ListView):
    model = Event
    template_name = 'sekai_app/events.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Event.objects.all()
        query = self.request.GET.get('query')
        group_filter = self.request.GET.get('group')
        date_filter = self.request.GET.get('start_date')

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if group_filter:
            queryset = queryset.filter(group__name__icontains=group_filter)

        if date_filter:
            queryset = queryset.filter(start_date=date_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'sekai_app/event_detail.html'
    context_object_name = 'event'



#Delete
@admin_token_required
def delete_object(request, model_class, pk, redirect_url, template_name='sekai_app/confirm_delete.html'):
    obj = get_object_or_404(model_class, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)
    return render(request, template_name, {'object': obj})


#CRUD World

@admin_token_required
def sekai_world_create(request):
    if request.method == 'POST':
        form = SekaiWorldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sekai_world_list')
    else:
        form = SekaiWorldForm()
    return render(request, 'sekai_app/crud/sekai_world_form.html', {'form': form})
@admin_token_required
def sekai_world_update(request, pk):
    world = get_object_or_404(SekaiWorld, pk=pk)
    if request.method == 'POST':
        form = SekaiWorldForm(request.POST, request.FILES, instance=world)
        if form.is_valid():
            form.save()
            return redirect('sekai_world_detail', pk=pk)
    else:
        form = SekaiWorldForm(instance=world)
    return render(request, 'sekai_app/crud/sekai_world_form.html', {'form': form})
@admin_token_required
def sekai_world_delete(request, pk):
    return delete_object(request, SekaiWorld, pk, 'sekai_world_list')
@admin_token_required
# CRUD для Group
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'sekai_app/crud/group_form.html', {'form': form})
@admin_token_required
def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_detail', pk=pk)
    else:
        form = GroupForm(instance=group)
    return render(request, 'sekai_app/crud/group_form.html', {'form': form})
@admin_token_required
def group_delete(request, pk):
    return delete_object(request, Group, pk, 'group_list')
@admin_token_required
# CRUD для Character
def character_create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = CharacterForm()
    return render(request, 'sekai_app/crud/character_form.html', {'form': form})
@admin_token_required
def character_update(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES, instance=character)
        if form.is_valid():
            form.save()
            return redirect('character_detail', pk=pk)
    else:
        form = CharacterForm(instance=character)
    return render(request, 'sekai_app/crud/character_form.html', {'form': form})
@admin_token_required
def character_delete(request, pk):
    return delete_object(request, Character, pk, 'character_list')
@admin_token_required
# CRUD для Card
def card_create(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'sekai_app/crud/card_form.html', {'form': form})
@admin_token_required
def card_update(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_detail', pk=pk)
    else:
        form = CardForm(instance=card)
    return render(request, 'sekai_app/crud/card_form.html', {'form': form})
@admin_token_required
def card_delete(request, pk):
    return delete_object(request, Card, pk, 'card_list')
@admin_token_required
# CRUD для Песен
def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'sekai_app/crud/song_form.html', {'form': form})
@admin_token_required
def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_detail', pk=pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'sekai_app/crud/song_form.html', {'form': form})
@admin_token_required
def song_delete(request, pk):
    return delete_object(request, Song, pk, 'song_list')
@admin_token_required
# CRUD для Event
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'sekai_app/crud/event_form.html', {'form': form})
@admin_token_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'sekai_app/crud/event_form.html', {'form': form})
@admin_token_required
def event_delete(request, pk):
    return delete_object(request, Event, pk, 'event_list')



#admin рендеры
@admin_token_required
def admin_page(request):
    return render(request, 'sekai_app/admin/admin_home.html')
@admin_token_required
def admin_world_list(request):
    worlds = SekaiWorld.objects.all()
    return render(request, 'sekai_app/admin/admin_sekai_worlds.html', {'worlds': worlds})
@admin_token_required
def admin_character_list(request):
    characters = Character.objects.all()
    return render(request, 'sekai_app/admin/admin_characters.html', {'characters': characters})
@admin_token_required
def admin_group_list(request):
    groups = Group.objects.all()
    return render(request, 'sekai_app/admin/admin_groups.html', {'groups': groups})
@admin_token_required
def admin_card_list(request):
    cards = Card.objects.all()
    return render(request, 'sekai_app/admin/admin_cards.html', {'cards': cards})
@admin_token_required
def admin_song_list(request):
    songs = Song.objects.all()
    return render(request, 'sekai_app/admin/admin_songs.html', {'songs': songs})
@admin_token_required
def admin_event_list(request):
    events = Event.objects.all()
    return render(request, 'sekai_app/admin/admin_events.html', {'events': events})
@admin_token_required
def admin_sekai_items_list(request):
    items = SekaiItems.objects.all()
    return render(request, 'sekai_app/admin/admin_sekai_items.html', {'items': items})
@admin_token_required
def admin_sekai_items_create(request):
    if request.method == 'POST':
        form = SekaiItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_sekai_items_list')
    else:
        form = SekaiItemsForm()
    return render(request, 'sekai_app/crud/sekai_item_form.html', {'form': form})
@admin_token_required
def admin_sekai_items_update(request, pk):
    item = get_object_or_404(SekaiItems, pk=pk)
    if request.method == 'POST':
        form = SekaiItemsForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('admin_sekai_items_list')
    else:
        form = SekaiItemsForm(instance=item)
    return render(request, 'sekai_app/crud/sekai_item_form.html', {'form': form, 'item': item})
@admin_token_required
def admin_sekai_items_delete(request, pk):
    item = get_object_or_404(SekaiItems, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_sekai_items_list')
    return render(request, 'sekai_app/crud/items_confirm.html', {'item': item})

def admin_access_check(request):
    if request.COOKIES.get('admin_token') == ADMIN_TOKEN:
        return redirect('admin_page')
    if request.method == 'POST':
        code = request.POST.get('access_code')
        if code == SECRET_WORD:
            response = redirect('admin_page')
            response.set_cookie('admin_token', ADMIN_TOKEN, max_age=86400)
            return response
        else:
            return redirect('home')
    return render(request, 'sekai_app/admin/admin_access_check.html')

def custom_404(request,exception):
    return render(request, '404.html', status=404)



