# Generated by Django 3.2 on 2021-04-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_analyticsresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyticsresult',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]