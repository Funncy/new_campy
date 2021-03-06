# Generated by Django 2.1.7 on 2019-07-10 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='영역이름')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='커뮤니티이름')),
            ],
        ),
        migrations.CreateModel(
            name='CompletionDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='영역이름')),
                ('group_name', models.CharField(max_length=10, verbose_name='그룹이름')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='학과이름')),
                ('college_name', models.CharField(max_length=20, verbose_name='단과대학이름')),
                ('community', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.Community', verbose_name='커뮤니티그룹')),
                ('same_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.Department', verbose_name='동일학과')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='트랙이름')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='대학이름')),
                ('maximum_credit', models.FloatField(verbose_name='최대학점')),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University', verbose_name='대학'),
        ),
        migrations.AddField(
            model_name='department',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University', verbose_name='대학'),
        ),
        migrations.AddField(
            model_name='completiondivision',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University', verbose_name='대학'),
        ),
        migrations.AddField(
            model_name='area',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University', verbose_name='대학'),
        ),
    ]
