# Generated by Django 4.2.16 on 2024-11-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekai_app', '0006_remove_gamestuff_description_remove_gamestuff_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestuff',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='gamestuff',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]