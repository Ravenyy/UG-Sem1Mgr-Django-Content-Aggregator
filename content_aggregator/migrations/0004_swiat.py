# Generated by Django 3.2.9 on 2022-01-29 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_aggregator', '0003_polskie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swiat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
    ]
