# Exercícios — Aula 4: Ambientes virtuais e gerenciamento de dependências

1. Crie um ambiente virtual novo em uma pasta de teste, ative-o, e
   confirme com `pip list` que ele começa praticamente vazio.

2. Instale a biblioteca `requests` nesse ambiente e gere um
   `requirements.txt` com `pip freeze > requirements.txt`. Abra o arquivo
   gerado e observe o formato.

3. Desative o ambiente virtual (`deactivate`), tente importar `requests`
   fora dele em um script Python, e observe o erro. Depois reative o
   ambiente e confirme que a importação funciona.

4. Delete a pasta do ambiente virtual (ela é totalmente recriável) e
   recrie-a a partir do `requirements.txt` gerado no exercício 2, usando
   `pip install -r requirements.txt`. Confirme que `requests` está
   instalado de novo.

5. No ambiente virtual deste curso, rode `pip show pytest` e identifique
   a versão instalada e de quais outros pacotes ele depende.

6. **Desafio:** pesquise a diferença entre fixar a versão exata
   (`requests==2.31.0`) e usar uma faixa de versões
   (`requests>=2.28,<3.0`) no `requirements.txt`. Escreva, em um
   comentário, quando cada abordagem faz mais sentido.

---
⬅️ [Voltar para a aula](aula.md) · ⬅️ [Voltar ao índice do módulo](../README.md)
