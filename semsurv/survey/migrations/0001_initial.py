# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 16:01
from __future__ import unicode_literals

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
            name='Grouping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('str_value', models.CharField(blank=True, max_length=200)),
                ('int_value', models.IntegerField(blank=True)),
                ('float_value', models.FloatField(blank=True)),
                ('bool_value', models.BooleanField()),
                ('order', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('randomize', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('text', models.TextField()),
                ('q_type', models.CharField(choices=[('combo', 'Combo Box'), ('check', 'Check Boxes'), ('radio', 'Radio Buttons'), ('text', 'Text Field'), ('int', 'Integer Field'), ('scale', 'Scale'), ('nscale', 'Named Scale'), ('unit', 'Unit Int Field'), ('bool', 'Yes or No')], max_length=10)),
                ('depends_string', models.CharField(blank=True, max_length=200)),
                ('grouping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Grouping')),
                ('options', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.OptionGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('name', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_value', models.CharField(blank=True, max_length=200)),
                ('int_value', models.IntegerField(blank=True)),
                ('float_value', models.FloatField(blank=True)),
                ('bool_value', models.BooleanField()),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Question')),
                ('respondent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Respondent')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Triple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('predicate', models.CharField(max_length=255)),
                ('obj', models.CharField(max_length=255)),
                ('value', models.BooleanField()),
                ('choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Question')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='grouping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.OptionGroup'),
        ),
        migrations.AddField(
            model_name='grouping',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
        ),
    ]
