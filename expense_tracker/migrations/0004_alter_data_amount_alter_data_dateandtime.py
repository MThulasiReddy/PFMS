# Generated by Django 4.1.4 on 2022-12-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0003_alter_data_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='dateandtime',
            field=models.DateField(),
        ),
    ]