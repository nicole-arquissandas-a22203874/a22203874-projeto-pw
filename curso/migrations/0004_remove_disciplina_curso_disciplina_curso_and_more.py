# Generated by Django 4.0.6 on 2024-06-09 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_disciplina_curso_alter_disciplina_linguagens_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='curso',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='curso',
            field=models.ManyToManyField(related_name='disciplinas', to='curso.curso'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='linguagens',
            field=models.ManyToManyField(related_name='disciplinas', to='curso.linguagemprogramacao'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='linguagensProgramacao',
            field=models.ManyToManyField(related_name='projetos', to='curso.linguagemprogramacao'),
        ),
    ]