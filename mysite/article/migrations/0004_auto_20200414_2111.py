# Generated by Django 3.0.3 on 2020-04-14 13:11

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200414_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='body',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
