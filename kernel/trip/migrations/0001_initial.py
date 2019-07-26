# Generated by Django 2.1.7 on 2019-04-11 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('deadline', models.DateField()),
                ('available', models.BooleanField(default=True)),
                ('precentage', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road', models.CharField(max_length=128, unique=True, verbose_name='road')),
                ('url', models.SlugField(help_text='url accessibilty', max_length=128, verbose_name='slug')),
                ('distance', models.PositiveIntegerField(default=0, help_text='based on kilometer.')),
                ('price', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True, help_text='if you want to deactivate this road, please make it false.')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('across', models.ManyToManyField(related_name='distance', to='trip.City')),
                ('city1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city1', to='trip.City')),
                ('city2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city2', to='trip.City')),
            ],
            options={
                'verbose_name': 'Distance',
                'verbose_name_plural': 'Distances',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('is_traditional', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='trip.City')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(choices=[(1, 'front seat'), (2, 'left seat'), (3, 'middle seat'), (4, 'right seat')], null=True, verbose_name='position')),
                ('state', models.PositiveSmallIntegerField(choices=[(1, 'singular'), (2, 'plural')], null=True, verbose_name='state')),
                ('init_price', models.PositiveIntegerField(null=True, verbose_name='price')),
                ('paid_price', models.PositiveIntegerField(null=True, verbose_name='paid_price')),
                ('type_price', models.SmallIntegerField(choices=[(1, 'cash'), (2, 'online')], default=2, null=True)),
                ('discount', models.CharField(max_length=64, null=True, verbose_name='discount')),
            ],
            options={
                'verbose_name': 'Seats',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'pending'), (2, 'done')], verbose_name='status')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('d', "don't care")], default='d', max_length=1, verbose_name='gender')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_dest', to='trip.City', verbose_name='destination')),
                ('destination_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_reg_dest', to='trip.Region', verbose_name='destination region')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trip', to=settings.AUTH_USER_MODEL, verbose_name='driver')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_origin', to='trip.City', verbose_name='origin')),
                ('origin_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_reg_origin', to='trip.Region', verbose_name='origin region')),
            ],
            options={
                'verbose_name': 'trip',
                'verbose_name_plural': 'trips',
                'ordering': ('status', '-start_time'),
            },
        ),
        migrations.AddField(
            model_name='seat',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seat', to='trip.Trip', verbose_name='trip'),
        ),
        migrations.AddField(
            model_name='seat',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('position', 'trip')},
        ),
        migrations.AddIndex(
            model_name='distance',
            index=models.Index(fields=['url'], name='trip_distan_url_b41c95_idx'),
        ),
    ]