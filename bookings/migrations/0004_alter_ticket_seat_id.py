# Generated by Django 3.2.6 on 2021-08-26 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_seat_seat for a show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.seat'),
        ),
    ]
