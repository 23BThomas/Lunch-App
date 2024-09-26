# Generated by Django 3.2.25 on 2024-09-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('meals_taken', models.PositiveIntegerField(default=0)),
                ('meals_remaining', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
