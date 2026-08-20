# Exercícios — Aula 2: Exceções customizadas

1. Crie uma exceção `IdadeInvalidaError` e use-a em uma função
   `cadastrar_pessoa(nome, idade)` que a levanta se `idade < 0`.

2. Crie uma exceção `SenhaFracaError` e use-a em uma função
   `validar_senha(senha)` que a levanta se a senha tiver menos de 8
   caracteres, incluindo na mensagem o tamanho mínimo exigido.

3. Crie uma hierarquia com uma exceção base `ErroFormulario` e duas
   específicas, `CampoObrigatorioError` e `FormatoInvalidoError`, ambas
   herdando da base. Escreva uma função de validação que levanta cada
   uma dependendo do problema encontrado.

4. Escreva um `try`/`except` que capture a exceção base `ErroFormulario`
   do exercício 3 e trate ambos os casos específicos de forma unificada
   (uma única mensagem genérica de "formulário inválido").

5. Adicione um atributo extra a `CampoObrigatorioError` (por exemplo,
   `nome_do_campo`) e use-o para exibir qual campo especificamente
   estava faltando.

6. **Desafio:** modele um sistema de reservas com uma exceção base
   `ErroReserva`, e duas específicas: `HorarioIndisponivelError` (com
   atributo `horario`) e `CapacidadeExcedidaError` (com atributos
   `capacidade_maxima` e `quantidade_solicitada`). Escreva uma função
   `fazer_reserva(...)` que levanta a exceção apropriada, e um bloco de
   tratamento que trata cada uma com uma mensagem específica, mas
   também um `except ErroReserva` mais genérico como último recurso.

---
⬅️ [Voltar para a aula](aula.md)
