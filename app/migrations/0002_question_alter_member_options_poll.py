# Generated by Django 4.0.4 on 2022-04-15 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text of question')),
                ('type', models.CharField(choices=[('1', models.CharField()), ('2', '2')], max_length=2, verbose_name='Type of question')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Member', 'verbose_name_plural': 'Members'},
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Title')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('description', models.TextField(verbose_name='Description')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='app.member', verbose_name='Member')),
            ],
            options={
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Polls',
            },
        ),
    ]
