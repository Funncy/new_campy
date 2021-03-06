# Generated by Django 2.1.7 on 2019-07-10 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuleGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='졸업요건명')),
                ('type', models.CharField(max_length=20, verbose_name='졸업요건타입')),
                ('value', models.SmallIntegerField(default=0, verbose_name='졸업요건값')),
            ],
        ),
        migrations.CreateModel(
            name='RuleSpecific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='졸업요건명')),
                ('type', models.CharField(max_length=20, verbose_name='졸업요건타입')),
                ('value', models.SmallIntegerField(default=0, verbose_name='졸업요건값')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='그룹명')),
                ('completion_divisions', models.ManyToManyField(to='university.CompletionDivision', verbose_name='이수구분들')),
            ],
        ),
        migrations.AddField(
            model_name='rulespecific',
            name='subject_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graduation.SubjectGroup', verbose_name='과목그룹'),
        ),
        migrations.AddField(
            model_name='rulespecific',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Track', verbose_name='트랙'),
        ),
        migrations.AddField(
            model_name='rulespecific',
            name='upper_rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='graduation.RuleGeneral', verbose_name='상위졸업요건'),
        ),
        migrations.AddField(
            model_name='rulegeneral',
            name='subject_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graduation.SubjectGroup', verbose_name='과목그룹'),
        ),
        migrations.AddField(
            model_name='rulegeneral',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Track', verbose_name='트랙'),
        ),
    ]
