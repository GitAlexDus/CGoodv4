# Generated by Django 4.1.7 on 2023-05-09 12:09

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
            name='Casier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CasNum', models.PositiveIntegerField()),
                ('CasObj', models.CharField(max_length=200)),
                ('CasStatus', models.BooleanField(default=False)),
                ('CasTaille', models.CharField(max_length=200)),
                ('CasRqtStatusCode', models.CharField(max_length=200)),
                ('CasOpenCode', models.CharField(max_length=200)),
                ('CasComment', models.TextField(blank=True, null=True)),
                ('CasMqttTopic', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Placard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaNom', models.CharField(max_length=200)),
                ('PlaPhoto', models.CharField(blank=True, max_length=200, null=True)),
                ('PlaRqtStatusCode', models.CharField(blank=True, max_length=200, null=True)),
                ('PlaOpenAllCode', models.CharField(blank=True, max_length=200, null=True)),
                ('PlaComment', models.TextField(blank=True, null=True)),
                ('PlaStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Resa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResDate', models.DateField(verbose_name='Date de la reservation - AAAA-MM-JJ')),
                ('ResHeure', models.TimeField(verbose_name='Heure de la reservation - HH:mm')),
                ('ResNbreHeure', models.DurationField(default=1)),
                ('ResPIN', models.CharField(max_length=200)),
                ('ResStatus', models.PositiveIntegerField(default=1)),
                ('casier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.casier')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='casier',
            name='placard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.placard'),
        ),
    ]
