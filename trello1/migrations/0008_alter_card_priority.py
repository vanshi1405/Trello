# Generated by Django 4.0.6 on 2023-08-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello1', '0007_alter_card_lable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Low', max_length=10),
        ),
    ]