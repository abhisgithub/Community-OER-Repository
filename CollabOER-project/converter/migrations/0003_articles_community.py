# Generated by Django 2.0.5 on 2018-06-13 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_articles_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='community',
            field=models.CharField(default='0000', max_length=50),
        ),
    ]
