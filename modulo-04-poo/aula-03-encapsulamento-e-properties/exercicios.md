# Exercícios — Aula 3: Encapsulamento e properties

1. Crie uma classe `Pessoa` com uma `@property` `idade` que não permite
   valores negativos (levanta `ValueError` se tentarem atribuir).

2. Crie uma classe `Temperatura` que guarda a temperatura em Celsius
   internamente (`_celsius`), mas expõe duas properties somente leitura:
   `fahrenheit` e `kelvin`, calculadas a partir de `_celsius`.

3. Crie uma classe `Produto` com uma property `preco` que, ao ser
   definida, arredonda automaticamente o valor para 2 casas decimais
   (`round(valor, 2)`) em vez de rejeitar.

4. Adicione a uma classe `Usuario` uma property `email` cujo setter
   valida que o valor contém um `"@"`, levantando `ValueError` caso
   contrário.

5. Explique, em um comentário, por que o código abaixo entra em loop
   infinito e cause um erro (`RecursionError`) se executado:
   ```python
   class Exemplo:
       @property
       def valor(self):
           return self.valor    # BUG proposital
   ```

6. **Desafio:** crie uma classe `Carrinho` com uma lista interna de
   itens (protegida, `_itens`) e uma property `total` (somente leitura)
   que retorna a soma dos preços de todos os itens. Adicione um método
   `adicionar_item(nome, preco)` que valida `preco >= 0` antes de
   adicionar.

---
⬅️ [Voltar para a aula](aula.md)
