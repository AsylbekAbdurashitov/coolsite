# Generated by Django 4.2.8 on 2023-12-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_actor_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='salary',
            field=models.FloatField(blank=True, null=True),
        ),
    ]