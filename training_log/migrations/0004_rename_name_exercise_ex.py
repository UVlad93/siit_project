# Generated by Django 3.2.4 on 2021-06-29 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_log', '0003_alter_traininglog_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='name',
            new_name='ex',
        ),
    ]
