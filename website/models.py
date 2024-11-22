from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    tar_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, db_column='tar_descricao')
    setor = models.CharField(max_length=100, db_column='tar_setor')
    prioridade = models.CharField(max_length=20, db_column='tar_prioridade')
    status = models.CharField(max_length=20, db_column='tar_status')
    data = models.DateField(db_column='tar_data')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'tbl_tarefas'