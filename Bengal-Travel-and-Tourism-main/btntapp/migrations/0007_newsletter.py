# Generated by Django 3.0.2 on 2020-04-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btntapp', '0006_auto_20200407_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]