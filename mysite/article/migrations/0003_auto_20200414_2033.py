# Generated by Django 3.0.3 on 2020-04-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200414_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='body',
            field=models.TextField(),
        ),
    ]