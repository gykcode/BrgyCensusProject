# Generated by Django 4.2.1 on 2023-07-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_censusnewformmodel_additional_booklet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='censusnewformmodel',
            name='additional_booklet',
            field=models.CharField(blank=True, choices=[('1', 'Yes, use additional booklet'), ('2', 'None')], default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='censusnewformmodel',
            name='birth_registered_1',
            field=models.CharField(blank=True, choices=[('Yes', '1: YES'), ('No', '2: NO')], default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='censusnewformmodel',
            name='copy_birthcert_1',
            field=models.CharField(blank=True, choices=[('Yes', '1: YES'), ('No', '2: NO')], default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='censusnewformmodel',
            name='marital_status_1',
            field=models.CharField(choices=[('1', 'SINGLE'), ('2', 'MARRIED'), ('3', 'COMMON LAW/ LIVE-IN'), ('4', 'WIDOWED'), ('5', 'DIVORCED/ SEPARATED/ ANNULLED')], default='1', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='censusnewformmodel',
            name='not_yet_listed',
            field=models.CharField(blank=True, choices=[('1', 'Yes, add to the list'), ('2', 'None')], default='', max_length=4, null=True),
        ),
    ]