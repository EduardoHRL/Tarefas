# Generated by Django 5.1.2 on 2024-11-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_usuario_tarefa_user_alter_tarefa_prioridade_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='user',
            new_name='usuario',
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='prioridade',
            field=models.CharField(db_column='tar_prioridade', max_length=20),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(db_column='tar_status', max_length=20),
        ),
    ]