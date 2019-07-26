# Generated by Django 2.2.3 on 2019-07-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0010_auto_20190422_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='passenger_capacity',
            field=models.PositiveSmallIntegerField(choices=[(1, 'تک سرنشین'), (2, 'دو سرنشین'), (3, 'سه سرنشین'), (4, 'چهار سرنشین')], null=True, verbose_name='passenger_capacity'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(1, 'صحیح'), (2, 'لغو')], default=1, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'در حال اجرا'), (2, 'تمام شده')], verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='type_creator',
            field=models.PositiveSmallIntegerField(choices=[(1, 'راننده'), (2, 'مسافر')], verbose_name='creator type'),
        ),
    ]
