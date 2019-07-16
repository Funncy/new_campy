# Generated by Django 2.1.7 on 2019-07-16 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_auto_20190715_2023'),
        ('graduation', '0007_auto_20190717_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='rulespecific',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.Department', verbose_name='학과'),
            preserve_default=False,
        ),
    ]
