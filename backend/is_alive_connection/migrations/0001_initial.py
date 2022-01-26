# Generated by Django 4.0.1 on 2022-01-26 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('system', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('create_time', models.DateTimeField()),
                ('remove_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusHistory',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('entry_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='is_alive_connection.entry')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='is_alive_connection.status')),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('entry_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='is_alive_connection.entry')),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.CharField(max_length=24)),
                ('private_key', models.CharField(max_length=128)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='is_alive_connection.entry')),
            ],
        ),
    ]
