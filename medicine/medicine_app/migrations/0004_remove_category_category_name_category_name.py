# Generated by Django 4.2 on 2023-05-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_app', '0003_medicine_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='jajo', max_length=64),
            preserve_default=False,
        ),
    ]