# Generated by Django 2.1 on 2019-07-09 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_monster_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monster',
            name='skills',
        ),
    ]
