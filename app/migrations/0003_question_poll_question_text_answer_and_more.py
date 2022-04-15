# Generated by Django 4.0.4 on 2022-04-15 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_question_alter_member_options_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Poll', to='app.poll', verbose_name='Poll'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='text_answer',
            field=models.TextField(default=1, verbose_name='Answer with text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('1', 'Answer with text'), ('2', 'Answer with choice'), ('3', 'Answer with some choices')], max_length=2, verbose_name='Type of question'),
        ),
        migrations.CreateModel(
            name='ChoiceSomeAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Answer with some choices')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.poll', verbose_name='Poll')),
            ],
            options={
                'verbose_name': 'Choice some answers',
                'verbose_name_plural': 'Choice some answers',
            },
        ),
        migrations.CreateModel(
            name='ChoiceAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Answer with choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='app.poll', verbose_name='Poll')),
            ],
            options={
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choices',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='choice_answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='app.choicesomeanswer', verbose_name='Answer with some choices'),
            preserve_default=False,
        ),
    ]