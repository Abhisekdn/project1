# Generated by Django 2.2.2 on 2019-07-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190703_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(null=True, to='home.Book'),
        ),
    ]
