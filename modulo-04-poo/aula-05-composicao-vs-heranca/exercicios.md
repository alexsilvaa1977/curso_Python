# Exercícios — Aula 5: Composição vs. herança

1. Modele `Computador` e `ProcessadorCPU` usando composição
   (`Computador` tem um `ProcessadorCPU`), com um método
   `ligar()` no `Computador` que usa o processador.

2. Dado o exemplo problemático de `Pinguim` herdando de `Voador`, escreva
   (em um comentário) outra situação do dia a dia com o mesmo problema
   (uma subclasse que precisa "desligar" comportamento herdado).

3. Modele `Biblioteca` e `Livro` usando composição: `Biblioteca` tem uma
   lista de `Livro`, com um método `total_livros()`.

4. Reescreva a hierarquia problemática abaixo usando composição:
   ```python
   class Impressora:
       def imprimir(self):
           return "imprimindo..."

   class ImpressoraSemTinta(Impressora):
       def imprimir(self):
           raise RuntimeError("Sem tinta!")
   ```
   (dica: uma impressora "tem" um nível de tinta, que pode ou não
   permitir imprimir — isso não deveria ser uma subclasse separada).

5. Para os pares abaixo, decida se a relação é "é um" (herança) ou "tem
   um" (composição), com uma frase de justificativa para cada:
   `Gato`/`Animal`, `Carro`/`Rodas`, `Gerente`/`Funcionario`,
   `Pedido`/`ClienteQueFezOPedido`.

6. **Desafio:** modele um sistema de personagens de jogo onde
   `Personagem` **tem uma** `Arma` (composição) em vez de ter
   subclasses fixas como `PersonagemComEspada`, `PersonagemComArco`. A
   `Arma` deve ter um método `atacar()`, e trocar a arma de um
   personagem deve ser tão simples quanto reatribuir o atributo.

---
⬅️ [Voltar para a aula](aula.md) · ⬅️ [Voltar ao índice do módulo](../README.md)
