# Generated by Django 4.1.2 on 2022-10-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notification_post_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('followers', 'followers'), ('post_like', 'post_like'), ('comment', 'comment')], max_length=20),
        ),
    ]