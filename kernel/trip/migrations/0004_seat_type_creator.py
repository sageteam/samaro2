# Generated by Django 2.1.7 on 2019-04-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_trip_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='type_creator',
            field=models.PositiveSmallIntegerField(choices=[(1, 'driver'), (2, 'passenger')], default=1, verbose_name='creator type'),
            preserve_default=False,
        ),
    ]