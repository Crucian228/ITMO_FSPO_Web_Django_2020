# Generated by Django 3.0.6 on 2020-06-06 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200606_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='id_crew_member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.crew_member'),
        ),
        migrations.AddField(
            model_name='flight',
            name='id_flight',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.flight_information'),
        ),
        migrations.AddField(
            model_name='flight',
            name='id_helicopter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.helicopter'),
        ),
    ]
