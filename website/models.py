from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    usu_codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, db_column='usu_nome')
    email = models.EmailField(max_length=255, db_column='usu_email')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tbl_usuarios'



class Tarefa(models.Model):
    tar_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, db_column='tar_descricao')
    setor = models.CharField(max_length=100, db_column='tar_setor')
    prioridade = models.CharField(max_length=20, db_column='tar_prioridade')
    status = models.CharField(max_length=20, db_column='tar_status')
    data = models.DateField(db_column='tar_data')
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='tarefas', db_column='usu_codigo'
    )

    class Meta:
        db_table = 'tbl_tarefas'


class Login(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.conteudo[:50]} - {self.usuario.username}"

