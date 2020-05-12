# Generated by Django 3.0.6 on 2020-05-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_settings', '0004_auto_20200512_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
