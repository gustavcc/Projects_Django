# Generated by Django 5.0.2 on 2024-03-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_question_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer_1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_5',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_a',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_b',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_c',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_d',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_e',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct',
            field=models.CharField(choices=[('A', 'A)'), ('B', 'B)'), ('C', 'C)'), ('D', 'D)'), ('E', 'E)')], max_length=8),
        ),
    ]
