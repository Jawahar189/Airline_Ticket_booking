# Generated by Django 4.2.1 on 2023-10-10 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_bookings_train_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='Train_no',
            new_name='train_no',
        ),
    ]
