# Generated by Django 4.2 on 2023-05-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_app', '0002_remove_category_slug_remove_medicine_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='category',
            field=models.ManyToManyField(to='medicine_app.category'),
        ),
    ]