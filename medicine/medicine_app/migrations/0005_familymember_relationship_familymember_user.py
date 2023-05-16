# Generated by Django 4.2 on 2023-05-12 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine_app', '0004_remove_category_category_name_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='relationship',
            field=models.CharField(default='kura', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familymember',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
