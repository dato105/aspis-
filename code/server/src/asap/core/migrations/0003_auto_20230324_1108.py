# Generated by Django 3.2.9 on 2023-03-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230323_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='statusAlert',
            field=models.TextField(choices=[('new requests', 'Statues 0'), ('opening a process', 'Statues 1'), ('establishment of a ptofessional committee', 'Statues 2'), ('professional committee', 'Statues 3'), ('final appointments committee', 'Statues 4'), ('requests for the CHE', 'Statues 5')], default=None, max_length=65),
        ),
    ]