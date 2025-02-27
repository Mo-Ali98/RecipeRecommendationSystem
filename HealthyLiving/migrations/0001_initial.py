# Generated by Django 2.2.6 on 2020-03-23 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('categories', models.TextField()),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('calories', models.IntegerField()),
                ('words', models.TextField()),
                ('onestarRating', models.IntegerField(default=0)),
                ('twostarRating', models.IntegerField(default=0)),
                ('threestarRating', models.IntegerField(default=0)),
                ('fourstarRating', models.IntegerField(default=0)),
                ('fivestarRating', models.IntegerField(default=0)),
                ('totalRatings', models.IntegerField(default=0)),
                ('avgRating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RecentlyViewed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('recipeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthyLiving.Recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-Date',),
            },
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('rating', models.IntegerField(default=0)),
                ('recipeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthyLiving.Recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-rating',),
            },
        ),
    ]
