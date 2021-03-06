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
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_acc_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='bank acc name')),
                ('bank_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='bank name')),
                ('bank_sheba', models.CharField(blank=True, max_length=128, null=True, verbose_name='bank sheba')),
                ('bank_card', models.CharField(blank=True, max_length=128, null=True, verbose_name='bank card')),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(blank=True, max_length=128, null=True, verbose_name='job')),
                ('job_place', models.CharField(blank=True, max_length=128, null=True, verbose_name='job_place')),
                ('emergency_number', models.CharField(blank=True, max_length=128, null=True, verbose_name='emergency_number')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='name')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='GeneralProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], default='m', max_length=1, null=True, verbose_name='gender')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth_date')),
                ('national_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='national_code')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='tel')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='mobile')),
                ('adr', models.CharField(blank=True, max_length=256, null=True, verbose_name='adr')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='postal_code')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='profile/user/', verbose_name='pic')),
                ('national_code_pic', models.ImageField(blank=True, null=True, upload_to='profile/user/', verbose_name='national_code_pic')),
                ('edu_degree', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'diploma'), (2, 'associate'), (3, 'bachelor'), (4, 'master'), (5, 'phd')], null=True, verbose_name='edu_degree')),
                ('about', models.TextField(blank=True, null=True, verbose_name='about')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='name')),
                ('color', models.CharField(blank=True, max_length=32, null=True, verbose_name='color')),
                ('model', models.CharField(blank=True, max_length=32, null=True, verbose_name='model')),
                ('plaque', models.CharField(blank=True, max_length=8, null=True, verbose_name='plaque')),
                ('year', models.DateField(blank=True, null=True, verbose_name='year')),
                ('chassis_number', models.CharField(blank=True, max_length=64, null=True, verbose_name='chassis')),
                ('driver_card', models.ImageField(blank=True, null=True, upload_to='profile/driver/', verbose_name='driver card')),
                ('machine_card', models.ImageField(blank=True, null=True, upload_to='profile/driver/', verbose_name='machine card')),
                ('misdiagnosis', models.ImageField(blank=True, null=True, upload_to='profile/driver/', verbose_name='misdiagnosis')),
                ('car_pic', models.ImageField(blank=True, null=True, upload_to='profile/driver/', verbose_name='car pic')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='machine', to='users.Driver', verbose_name='driver')),
                ('features', models.ManyToManyField(related_name='machine', to='users.Feature', verbose_name='features')),
            ],
            options={
                'verbose_name': 'Machine',
                'verbose_name_plural': 'Machines',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(choices=[('p', 'positive'), ('t', 'negative')], max_length=1, verbose_name='point')),
                ('summary', models.CharField(max_length=512, verbose_name='summary')),
                ('seen', models.BooleanField(default=False, verbose_name='seen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(blank=True, max_length=128, null=True, verbose_name='job')),
                ('emergency_number', models.CharField(blank=True, max_length=128, null=True, verbose_name='emergency_number')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to='users.GeneralProfile', verbose_name='profile')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_message_from', models.CharField(choices=[('e', 'email'), ('t', 'ticket')], default='e', max_length=1, verbose_name='get message from')),
                ('subscribe', models.BooleanField(default=0, verbose_name='subscribe')),
                ('email_transaction', models.BooleanField(default=0, verbose_name='email transaction')),
                ('email_trip_info', models.BooleanField(default=0, verbose_name='email trip info')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='setting', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Transmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(blank=True, max_length=128, null=True, verbose_name='job')),
                ('emergency_number', models.CharField(blank=True, max_length=128, null=True, verbose_name='emergency_number')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transmit', to='users.GeneralProfile', verbose_name='profile')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='users.GeneralProfile', verbose_name='profile'),
        ),
        migrations.AddField(
            model_name='bank',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank', to='users.Driver', verbose_name='driver'),
        ),
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together={('user', 'title')},
        ),
    ]
