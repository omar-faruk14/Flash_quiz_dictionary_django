# Generated by Django 4.2.2 on 2023-06-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlashWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('meaning', models.CharField(max_length=100)),
                ('example', models.TextField()),
                ('kanji', models.CharField(max_length=100)),
            ],
        ),
    ]
