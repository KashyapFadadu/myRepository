# Generated by Django 4.2.3 on 2023-08-03 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programmers',
            name='id',
        ),
        migrations.AlterField(
            model_name='programmers',
            name='Prog_Group_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
