# Generated by Django 4.2 on 2023-04-25 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0005_auto_20230401_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='employment_stage',
        ),
        migrations.RemoveField(
            model_name='application',
            name='stage_due_date',
        ),
        migrations.AddField(
            model_name='profile',
            name='employment_stage',
            field=models.TextField(choices=[('A', 'Stage 0'), ('B', 'Stage 1'), ('C', 'Stage 2')], default=None,
                                   max_length=70),
        ),
        migrations.AddField(
            model_name='profile',
            name='stage_due_date',
            field=models.DateTimeField(default=None),
        ),
    ]