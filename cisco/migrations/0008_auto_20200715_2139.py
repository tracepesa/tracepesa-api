# Generated by Django 3.0.8 on 2020-07-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cisco', '0007_auto_20200715_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciscorouter',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]