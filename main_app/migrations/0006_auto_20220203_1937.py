# Generated by Django 3.2.9 on 2022-02-03 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_merge_20220131_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='industry',
            field=models.CharField(choices=[('AERO', 'Aerospace'), ('A', 'Art'), ('AUTO', 'Automotive'), ('D', 'Design'), ('EDU', 'Education'), ('E', 'Engineering'), ('F', 'Finance'), ('G', 'Government'), ('H', 'Healthcare'), ('IT', 'Information Technology'), ('M', 'Media & Entertainment'), ('SCI', 'Science'), ('S', 'Service Industry'), ('RE', 'Real Estate & Development'), ('R', 'Retail')], default='AERO', max_length=10),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_title',
            field=models.ManyToManyField(to='main_app.JobTitle'),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job_title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
