# Generated by Django 3.1.13 on 2023-09-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_auto_20230923_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='nationality',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]