# Generated by Django 2.1.7 on 2019-02-18 00:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iamshakti', '0008_jtmuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jtmuser',
            old_name='text',
            new_name='interests',
        ),
        migrations.RemoveField(
            model_name='jtmuser',
            name='name',
        ),
        migrations.AddField(
            model_name='jtmuser',
            name='firstName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jtmuser',
            name='joindate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jtmuser',
            name='lastName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jtmuser',
            name='memberType',
            field=models.CharField(choices=[('ME', 'Member'), ('GA', 'General Ally')], default='GA', max_length=2),
        ),
    ]
