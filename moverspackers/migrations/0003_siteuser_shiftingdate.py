# Generated by Django 4.1 on 2023-03-05 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moverspackers', '0002_remove_siteuser_pro_remove_siteuser_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='shiftingdate',
            field=models.DateField(null=True),
        ),
    ]