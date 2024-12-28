# gpt-selenium
Pronto, você achou, um projeto que usa selenium pra automatizar o gpt que realmente funciona e é bem eficiente.

Aqui uso o Navegador que esta aqui nos meus repositórios para conseguir passar das seguransas do site do gpt, e ainda, podendo criar varias instancias caso queira, com um custo monetario nulo, custo de processamento baixissimo e muita diversão :)

https://github.com/user-attachments/assets/b5817daa-3783-46a8-bc6b-7e24b7c24d6f

# exemplo de uso
```python
import asyncio
from gpt_selenium.gpt import Modelos, Model

async def main() -> None:

  grupo:Modelos = Modelos(debug=False)

  model:Model = await grupo.create_model()

  while True:
    pergunta = input('perguntar (digite PARAR para encerrar) (digite LIMPAR para limpar o historico):\n')
    if pergunta == 'PARAR':
      break
    elif pergunta == 'LIMPAR':
      await model.clear_history()
      continue
    
    resp = await model.asq(pergunta)
    print(f'resposta: {resp}')

  await grupo.stop()

asyncio.run(main())
```
