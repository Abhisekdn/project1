# Generated by Django 2.2.2 on 2019-07-04 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20190703_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(null=True, to='home.Book'),
        ),
    ]
