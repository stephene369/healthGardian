# Generated by Django 5.0.2 on 2024-02-25 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]