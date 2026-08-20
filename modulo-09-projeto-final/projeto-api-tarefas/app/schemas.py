"""Schemas Pydantic: o formato dos dados que entram e saem pela API.

Separar o schema de entrada (o que o cliente envia) do de saída (o que a
API devolve) é uma boa prática: o cliente nunca precisa (nem deve)
enviar o `id` ou a data de criação -- esses campos são gerados pelo
servidor.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class TarefaEntrada(BaseModel):
    titulo: str
    descricao: str | None = None
    concluida: bool = False

    @field_validator("titulo")
    @classmethod
    def titulo_nao_pode_ser_vazio(cls, valor: str) -> str:
        if not valor.strip():
            raise ValueError("O título não pode ser vazio")
        return valor.strip()


class TarefaAtualizacao(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    concluida: bool | None = None


class TarefaSaida(BaseModel):
    id: int
    titulo: str
    descricao: str | None
    concluida: bool
    criada_em: datetime | None

    model_config = ConfigDict(from_attributes=True)
