# Generated by Django 4.1.7 on 2023-04-10 20:59

from django.db import migrations, models
import hospital.models.people


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_allergy_contract_illness_person_salaried_nurse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=models.ManyToManyField(blank=True, null=True, to='hospital.allergy'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='illnesses',
            field=models.ManyToManyField(blank=True, null=True, to='hospital.illness'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='primary_physician',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(hospital.models.people.get_chief_of_staff), to='hospital.physician'),
        ),
    ]
