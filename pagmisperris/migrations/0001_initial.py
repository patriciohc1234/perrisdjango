# Generated by Django 2.1.2 on 2018-10-23 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('codigoMascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombreMascota', models.CharField(max_length=20)),
                ('edadMascota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MascotaPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoMascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagmisperris.Mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rutPersona', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombrePersona', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateField()),
                ('direccionPersona', models.CharField(max_length=50)),
                ('numeroFono', models.CharField(blank=True, max_length=10, null=True)),
                ('emailPersona', models.CharField(max_length=50)),
                ('passwordPersona', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='mascotapersona',
            name='codigoPersona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagmisperris.Persona'),
        ),
    ]
