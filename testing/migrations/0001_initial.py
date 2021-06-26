# Generated by Django 3.2.4 on 2021-06-26 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Choose a title for your testing session', max_length=100)),
                ('mh_maw', models.IntegerField(help_text='Max Hangs- Maximum Added Weight (in kg)')),
                ('pu_maw', models.IntegerField(help_text='Maximum Added Weight Pull Up (in kg)')),
                ('fl', models.IntegerField(help_text='Maximum Front Lever Hold (in seconds)')),
                ('date_logged', models.DateField(default=django.utils.timezone.now, help_text='Date Logged')),
            ],
        ),
    ]
