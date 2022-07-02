# Generated by Django 4.0.5 on 2022-06-27 08:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_post_id_remove_post_user_post_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.TextField(),
        ),
    ]
