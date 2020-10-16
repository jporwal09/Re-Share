# Generated by Django 3.0.6 on 2020-10-16 13:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resource', '0002_auto_20201011_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='fav',
            field=models.ManyToManyField(related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
