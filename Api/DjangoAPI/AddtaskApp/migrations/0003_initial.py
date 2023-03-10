# Generated by Django 4.1.5 on 2023-01-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AddtaskApp', '0002_delete_addtasks_delete_assigntasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'done'), (1, 'pending'), (2, 'Not target')], default=2)),
                ('teamPic', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=30)),
                ('role', models.IntegerField(choices=[(0, 'admin'), (1, 'lead'), (2, 'user')])),
                ('request', models.IntegerField(default=0)),
                ('team', models.IntegerField(null=True)),
            ],
        ),
    ]
