# Generated by Django 4.1.2 on 2022-10-20 14:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='like_authors',
            field=models.ManyToManyField(related_name='like_recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]