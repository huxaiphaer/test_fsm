# Generated by Django 3.2 on 2021-04-29 13:10

from django.db import migrations, models
import django_logic.process


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('maintenance', 'Under maintenance'), ('locked', 'Locked'), ('open', 'Open')], default='open', max_length=16)),
                ('customer_received_notice', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=True)),
            ],
            bases=(django_logic.process.Process, models.Model),
        ),
    ]
