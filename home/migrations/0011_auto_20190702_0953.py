# Generated by Django 2.2.2 on 2019-07-02 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190702_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(null=True, to='home.Book'),
        ),
    ]
