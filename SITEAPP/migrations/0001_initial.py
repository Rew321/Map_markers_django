# Generated by Django 5.0.4 on 2024-04-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('lat', models.CharField(blank=True, max_length=200, null=True)),
                ('lng', models.CharField(blank=True, max_length=200, null=True)),
                ('place_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]