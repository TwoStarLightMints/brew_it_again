# Generated by Django 5.0.6 on 2024-07-21 03:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeRecipeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('grinder_setting', models.IntegerField()),
                ('ratio', models.CharField(max_length=6)),
                ('grams_coffee', models.IntegerField()),
                ('mili_water', models.IntegerField()),
                ('brew_time', models.CharField(max_length=6)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]