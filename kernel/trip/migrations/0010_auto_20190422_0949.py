# Generated by Django 2.1.7 on 2019-04-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0009_auto_20190421_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='discount',
            field=models.CharField(choices=[('15', '15%'), ('25', '25%'), ('50', '50%')], max_length=2, null=True, verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='gender',
            field=models.CharField(choices=[('m', 'مرد'), ('f', 'خانم'), ('d', 'مختلط')], default='d', max_length=1, verbose_name='gender'),
        ),
    ]
