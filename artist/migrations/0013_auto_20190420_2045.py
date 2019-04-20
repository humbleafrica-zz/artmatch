# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-20 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0012_auto_20190420_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('can_paint', models.BooleanField(default=False)),
                ('can_draw', models.BooleanField(default=False)),
                ('can_sing', models.BooleanField(default=False)),
                ('can_rap', models.BooleanField(default=False)),
                ('can_dance', models.BooleanField(default=False)),
                ('can_snap', models.BooleanField(default=False)),
                ('can_perform', models.BooleanField(default=False)),
                ('can_narrate', models.BooleanField(default=False)),
                ('can_playInst', models.BooleanField(default=False)),
                ('can_other', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Member's name")),
                ('talent', models.CharField(choices=[('pr', 'Painter'), ('mu', 'Musician'), ('dp', 'Drama/ Performance'), ('pt', 'poet/RAP'), ('pt', 'poet/RAP')], max_length=3)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.ArtGroup')),
            ],
        ),
        migrations.RenameField(
            model_name='work',
            old_name='craftid',
            new_name='work_id',
        ),
        migrations.RemoveField(
            model_name='work',
            name='is_favorite',
        ),
        migrations.AlterField(
            model_name='craft',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Artist'),
        ),
    ]
