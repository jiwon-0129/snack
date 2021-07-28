# Generated by Django 3.1.7 on 2021-07-24 05:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='eatingimages/')),
                ('name', models.CharField(max_length=200)),
                ('market_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('calories', models.CharField(max_length=200)),
                ('information', models.TextField()),
                ('purchase_link', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='reviewimages/')),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('salty_taste', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('sweet_taste', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('spicy_taste', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('eating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eating.eating')),
            ],
        ),
        migrations.AddField(
            model_name='eating',
            name='hashtag',
            field=models.ManyToManyField(blank=True, to='eating.HashTag'),
        ),
    ]