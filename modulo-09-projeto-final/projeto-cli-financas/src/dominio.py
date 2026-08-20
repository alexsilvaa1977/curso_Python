"""Camada de domínio: as regras de negócio do controle financeiro,
independentes de como os dados são salvos ou de como o usuário interage
com o programa (isso fica em persistencia.py e cli.py).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


class ValorInvalidoError(Exception):
    """Levantada quando o valor de uma transação é zero (não representa nem
    receita nem despesa, então não faz sentido registrá-lo).
    """


class TransacaoNaoEncontradaError(Exception):
    """Levantada ao tentar remover ou buscar uma transação com id inexistente."""


@dataclass
class Transacao:
    id: int
    descricao: str
    valor: float  # positivo = receita, negativo = despesa
    categoria: str = "geral"
    data: date = field(default_factory=date.today)

    def __post_init__(self):
        if self.valor == 0:
            raise ValorInvalidoError("O valor da transação não pode ser zero")

    @property
    def eh_receita(self) -> bool:
        return self.valor > 0

    def __str__(self) -> str:
        tipo = "receita" if self.eh_receita else "despesa"
        return f"#{self.id} [{self.data.isoformat()}] {self.descricao} ({self.categoria}, {tipo}): R$ {self.valor:.2f}"


class Carteira:
    """Guarda e organiza um conjunto de transações."""

    def __init__(self) -> None:
        self._transacoes: list[Transacao] = []
        self._proximo_id = 1

    def adicionar(
        self,
        descricao: str,
        valor: float,
        categoria: str = "geral",
        data: date | None = None,
    ) -> Transacao:
        transacao = Transacao(
            id=self._proximo_id,
            descricao=descricao,
            valor=valor,
            categoria=categoria,
            data=data or date.today(),
        )
        self._transacoes.append(transacao)
        self._proximo_id += 1
        return transacao

    def remover(self, id_transacao: int) -> None:
        transacao = self.buscar(id_transacao)
        self._transacoes.remove(transacao)

    def buscar(self, id_transacao: int) -> Transacao:
        for transacao in self._transacoes:
            if transacao.id == id_transacao:
                return transacao
        raise TransacaoNaoEncontradaError(
            f"Nenhuma transação encontrada com id {id_transacao}"
        )

    def listar(self, categoria: str | None = None) -> list[Transacao]:
        transacoes = self._transacoes
        if categoria is not None:
            transacoes = [t for t in transacoes if t.categoria == categoria]
        return sorted(transacoes, key=lambda t: t.data)

    def saldo(self) -> float:
        return sum(transacao.valor for transacao in self._transacoes)

    def total_receitas(self) -> float:
        return sum(t.valor for t in self._transacoes if t.eh_receita)

    def total_despesas(self) -> float:
        return sum(t.valor for t in self._transacoes if not t.eh_receita)

    def carregar_transacoes(self, transacoes: list[Transacao]) -> None:
        """Substitui as transações atuais por uma lista carregada (ex.: de um
        arquivo), ajustando o próximo id disponível de acordo.
        """
        self._transacoes = list(transacoes)
        self._proximo_id = max((t.id for t in transacoes), default=0) + 1

    def __len__(self) -> int:
        return len(self._transacoes)
