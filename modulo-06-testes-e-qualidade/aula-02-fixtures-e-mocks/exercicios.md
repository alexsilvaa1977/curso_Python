# Exercícios — Aula 2: Fixtures e mocks

1. Crie uma fixture `lista_de_numeros` que retorna `[1, 2, 3, 4, 5]`, e
   escreva dois testes que a usem (um verificando a soma, outro
   verificando o maior valor).

2. Adicione ao `test_conta.py` um teste que usa a fixture
   `conta_com_saldo` e verifica que `sacar()` levanta `ValueError` quando
   o valor pedido é maior que o saldo.

3. Crie uma fixture com `yield` que cria uma lista vazia antes do teste e
   imprime `"Teste finalizado"` depois (uma forma simples de observar o
   teardown acontecendo).

4. Escreva uma função `enviar_notificacao(servico_envio, mensagem)` que
   chama `servico_envio.enviar(mensagem)`. Teste-a passando um `Mock()`
   no lugar de `servico_envio`, e verifique com
   `servico_envio.enviar.assert_called_once_with(mensagem)` que o método
   foi chamado corretamente.

5. Use `monkeypatch` para simular `input()` retornando `"sim"`, e teste
   uma função `confirmar_acao()` que retorna `True` apenas se o usuário
   digitar exatamente `"sim"`.

6. **Desafio:** escreva uma função `buscar_usuario(id_usuario, cliente_http)`
   que chama `cliente_http.get(f"/usuarios/{id_usuario}")` e retorna
   `.json()`. Escreva um teste com um `Mock()` no lugar de
   `cliente_http`, configurando `.get.return_value.json.return_value`
   para simular uma resposta, e verifique que a função retorna os dados
   esperados sem fazer nenhuma chamada de rede real.

---
⬅️ [Voltar para a aula](aula.md)
