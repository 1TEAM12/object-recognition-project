<<<<<<< HEAD
# Generated by Django 4.1.2 on 2022-10-20 14:28
=======
# Generated by Django 4.1.2 on 2022-10-20 19:32
>>>>>>> 673e1b3429468cbcad61e4030ccddf964a878ebe

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
<<<<<<< HEAD
        ('recipe', '0001_initial'),
=======
>>>>>>> 673e1b3429468cbcad61e4030ccddf964a878ebe
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
<<<<<<< HEAD
            name='dessert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dessert_post', to='post.dessert'),
        ),
        migrations.AddField(
            model_name='post',
=======
>>>>>>> 673e1b3429468cbcad61e4030ccddf964a878ebe
            name='like_authors',
            field=models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
<<<<<<< HEAD
            model_name='dessert',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='recipe_dessert', to='recipe.recipe'),
        ),
        migrations.AddField(
=======
>>>>>>> 673e1b3429468cbcad61e4030ccddf964a878ebe
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post'),
        ),
    ]
