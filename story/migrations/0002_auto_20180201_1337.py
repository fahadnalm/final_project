# Generated by Django 2.0.1 on 2018-02-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='Text',
            new_name='text',
        ),
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='story', max_length=150),
            preserve_default=False,
        ),
    ]
