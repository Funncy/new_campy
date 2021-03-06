# Generated by Django 2.1.7 on 2019-07-16 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduation', '0002_auto_20190716_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rulegeneral',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University', verbose_name='대학'),
        ),
        migrations.AlterField(
            model_name='rulespecific',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University', verbose_name='대학'),
        ),
        migrations.AlterField(
            model_name='subjectgroup',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University', verbose_name='대학'),
        ),
    ]
