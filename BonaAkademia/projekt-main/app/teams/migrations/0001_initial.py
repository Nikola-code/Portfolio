# Generated by Django 4.1 on 2022-09-06 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortcut', models.CharField(max_length=64)),
                ('fullName', models.CharField(max_length=256)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='T_leader', to='workers.worker')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='T_team', to='teams.team')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='T_worker', to='workers.worker')),
            ],
        ),
    ]