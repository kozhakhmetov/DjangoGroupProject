# Generated by Django 2.2.8 on 2019-12-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191223_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
