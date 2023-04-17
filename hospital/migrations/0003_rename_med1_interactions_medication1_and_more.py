# Generated by Django 4.1.7 on 2023-04-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_skills_alter_interactions_severity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interactions',
            old_name='med1',
            new_name='medication1',
        ),
        migrations.RenameField(
            model_name='interactions',
            old_name='med2',
            new_name='medication2',
        ),
        migrations.AlterUniqueTogether(
            name='interactions',
            unique_together={('medication1', 'medication2')},
        ),
    ]
