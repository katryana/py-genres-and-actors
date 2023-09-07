# Generated by Django 4.0.2 on 2023-09-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='last_name',
        ),
    ]
