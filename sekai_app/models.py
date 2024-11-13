from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

class SekaiWorld(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.ImageField(upload_to='sekai_images', blank=True)
    background_image = models.ImageField(upload_to='sekai_backgrounds', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_groups(self):
        return self.groups.all()

    def get_items(self):
        return self.items.all()


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='group_images', blank=True)
    sekai = models.ForeignKey(SekaiWorld, on_delete=models.CASCADE, related_name='groups')
    background_image = models.ImageField(upload_to='group_backgrounds', blank=True,null=True)

    def __str__(self):
        return self.name

    def get_characters(self):
        return self.characters.all()

    def get_songs(self):
        return self.songs.all()


class Character(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='characters')
    description = models.TextField()
    sekai_type = models.CharField(max_length=255 , choices=[
        ('Game Character', 'Game Character'),
        ('Virtual Singer', 'Virtual Singer'),
    ])
    image = models.ImageField(upload_to='character_images', blank=True)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_cards(self):
        return self.cards.all()

    def get_songs(self):
        return self.songs.all()


class Card(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='cards')
    rarity = models.CharField(max_length=10, choices=[('1★', '1★'), ('2★', '2★'), ('3★', '3★'), ('4★', '4★'), ('Limited', 'Limited')])
    stats = models.TextField()
    image_url = models.ImageField(upload_to='card_images', blank=True)
    is_limited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.character.name} - {self.rarity}'


class Song(models.Model):
    GENRE_CHOICES = [
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('hip_hop', 'Hip Hop'),
        ('electronic', 'Electronic'),
        ('rnb', 'R&B'),
        ('country', 'Country'),
        ('blues', 'Blues'),
        ('reggae', 'Reggae'),
        ('latin', 'Latin'),
        ('folk', 'Folk'),
        ('metal', 'Metal'),
        ('punk', 'Punk'),
        ('indie', 'Indie'),
        ('disco', 'Disco'),
        ('soul', 'Soul'),
        ('funk', 'Funk'),
        ('house', 'House'),
        ('techno', 'Techno'),
        ('trance', 'Trance'),
        ('k_pop', 'K-Pop'),
        ('j_pop', 'J-Pop'),
        ('classical_cross', 'Classical Crossover'),
        ('opera', 'Opera'),
        ('instrumental', 'Instrumental'),
    ]

    name = models.CharField(max_length=100)
    artist = models.ManyToManyField(Character,related_name='songs')
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    animation = models.URLField(blank=True, null=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True, related_name='songs')
    image = models.ImageField(upload_to='song_images', blank=True)
    song_url = models.FileField(upload_to='song_files', blank=True , null=True)
    background_image = models.ImageField(upload_to='song_backgrounds', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_artist(self):
        return self.artist.all()


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images', blank=True)
    start_date = models.DateField()
    is_ended = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, related_name='events')
    character = models.ManyToManyField(Character, blank=True, related_name='events')
    character_cards = models.ManyToManyField(Card, blank=True, related_name='events')

    def __str__(self):
        return self.name


class GameStuff(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    video = models.FileField(upload_to='game_stuff_videos', blank=True, null=True)

class SekaiItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images', blank=True)
    sekai_world = models.ForeignKey(SekaiWorld, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='items', blank=True, null=True)

    def __str__(self):
        return self.name
