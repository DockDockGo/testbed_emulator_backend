# Generated by Django 4.2.7 on 2023-11-19 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testbed_emulator_backend_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amrstate',
            name='active_material_transport_task_chain',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='testbed_emulator_backend_app.materialtransporttaskchain'),
        ),
        migrations.AlterField(
            model_name='amrmission',
            name='amr_id',
            field=models.IntegerField(blank=True, choices=[(1, 'RICK'), (2, 'MORTY')], null=True),
        ),
        migrations.AlterField(
            model_name='amrstate',
            name='amr_id',
            field=models.IntegerField(blank=True, choices=[(1, 'RICK'), (2, 'MORTY')], null=True, unique=True),
        ),
    ]