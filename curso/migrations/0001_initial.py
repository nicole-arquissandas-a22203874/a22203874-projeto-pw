# Generated by Django 4.0.6 on 2024-04-07 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('apresentacao', models.TextField()),
                ('objetivos', models.TextField()),
                ('competencias', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=25)),
                ('ects', models.IntegerField()),
                ('curricularIUnitReadableCode', models.CharField(max_length=25)),
                ('areaCientifica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplinas', to='curso.areacientifica')),
            ],
        ),
        migrations.CreateModel(
            name='LinguagemProgramacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('descricao', models.TextField()),
                ('conceitosAplicados', models.TextField()),
                ('tecnologiasUsadas', models.TextField()),
                ('imagem', models.ImageField(null=True, upload_to='')),
                ('video_demo', models.URLField(blank=True, null=True)),
                ('repositorio_github', models.URLField(blank=True, null=True)),
                ('disciplina', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='curso.disciplina')),
                ('linguagensProgramacao', models.ManyToManyField(related_name='projetos', to='curso.linguagemprogramacao')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('disciplinas', models.ManyToManyField(related_name='docentes', to='curso.disciplina')),
            ],
        ),
    ]
