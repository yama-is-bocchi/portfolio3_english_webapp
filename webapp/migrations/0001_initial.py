# Generated by Django 4.1.7 on 2024-02-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20, verbose_name='英単語')),
                ('imi', models.CharField(max_length=20, verbose_name='意味')),
            ],
        ),
    ]
