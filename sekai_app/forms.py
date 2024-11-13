from django import forms
from .models import SekaiWorld, Group, Character, Card, Song, Event, SekaiItems


class SekaiWorldForm(forms.ModelForm):
    class Meta:
        model = SekaiWorld
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image_url': forms.FileInput(attrs={'class': 'form-control'}),
        }



class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'sekai': forms.Select(attrs={'class': 'form-control'}),
        }

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'sekai_type': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_popular': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        widgets = {
            'character': forms.Select(attrs={'class': 'form-control'}),
            'rarity': forms.Select(attrs={'class': 'form-control'}),
            'stats': forms.Textarea(attrs={'class': 'form-control'}),
            'image_url': forms.FileInput(attrs={'class': 'form-control'}),
            'is_limited': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'animation': forms.URLInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'song_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_ended': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'character': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'character_cards': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class SekaiItemsForm(forms.ModelForm):
    class Meta:
        model = SekaiItems
        fields = ['name', 'description', 'image', 'sekai_world','character']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'sekai_world': forms.Select(attrs={'class': 'form-control'}),
            'character': forms.Select(attrs={'class': 'form-control'}),
        }