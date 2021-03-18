# Generated by Django 3.1.7 on 2021-03-18 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_letivo', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.escola')),
                ('series', models.ManyToManyField(to='core.Serie')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Lotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professor')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.turma')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.serie'),
        ),
    ]
