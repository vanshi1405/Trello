# Generated by Django 4.0.6 on 2023-08-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello1', '0006_profile_user_type_alter_profile_job_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='lable',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]