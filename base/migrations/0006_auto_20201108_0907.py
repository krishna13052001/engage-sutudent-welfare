# Generated by Django 3.1.2 on 2020-11-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_studentannouncement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Faculty', 'Faculty'), ('Librarian', 'Librarian')], max_length=10, null=True),
        ),
    ]