# Generated by Django 4.2.1 on 2023-07-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_censusnewformmodel_acquisition_of_housing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='censusnewformmodel',
            name='additional_booklet',
            field=models.CharField(blank=True, choices=[('1', 'Yes, use additional booklet'), ('2', 'None')], default='', max_length=4),
        ),
        migrations.AddField(
            model_name='censusnewformmodel',
            name='age_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='censusnewformmodel',
            name='birth_registered_1',
            field=models.CharField(blank=True, choices=[('Yes', '1: YES'), ('No', '2: NO')], default='', max_length=4),
        ),
        migrations.AddField(
            model_name='censusnewformmodel',
            name='copy_birthcert_1',
            field=models.CharField(blank=True, choices=[('Yes', '1: YES'), ('No', '2: NO')], default='', max_length=4),
        ),
        migrations.AddField(
            model_name='censusnewformmodel',
            name='date_born_1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='censusnewformmodel',
            name='gender_1',
            field=models.CharField(blank=True, choices=[('1', 'MALE'), ('2', 'FEMALE')], default='', max_length=4),
        ),
        migrations.AddField(
            model_name='censusnewformmodel',
            name='marital_status_1',
            field=models.CharField(choices=[('1', 'SINGLE'), ('2', 'MARRIED'), ('3', 'COMMON LAW/ LIVE-IN'), ('4', 'WIDOWED'), ('5', 'DIVORCED/ SEPARATED/ ANNULLED')], default='1', max_length=4),
        ),
        migrations.AddField(
            model_name='censusnewformmodel',
            name='not_yet_listed',
            field=models.CharField(blank=True, choices=[('1', 'Yes, add to the list'), ('2', 'None')], default='', max_length=4),
        ),
        migrations.AddField(
            model_name='censusnewformmodel',
            name='relationship_to_head_1',
            field=models.CharField(blank=True, choices=[('1', 'Head'), ('2', 'Spouse of the head'), ('3', 'Never-married children of the head/spouse, from the oldest to the youngest'), ('4', 'Ever-married children of the head/spouse, from the oldest to the youngest'), ('5', 'Other relatives of the head'), ('6', 'Nonrelatives of the head')], default='', max_length=4),
        ),
        migrations.AddField(
            model_name='censusnewformmodel',
            name='residing_fullname_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]