# Generated by Django 4.2.16 on 2024-11-09 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekai_app', '0009_song_background_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SekaiItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='item_images')),
                ('sekai_world', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sekai_app.sekaiworld')),
            ],
        ),
    ]
