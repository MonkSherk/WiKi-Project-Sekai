# Generated by Django 4.2.16 on 2024-11-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekai_app', '0003_gamestuff'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestuff',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
