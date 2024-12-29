# gpt-selenium
Pronto, você achou, um projeto que usa selenium pra automatizar o gpt que realmente funciona e é bem eficiente.

Aqui uso o Navegador que esta aqui nos meus repositórios para conseguir passar das seguransas do site do gpt, e ainda, podendo criar varias instancias caso queira, com um custo monetario nulo, custo de processamento baixissimo e muita diversão :)

# como funciona?
Você não precisa de conta, não precisa de um pc potente, somente uma internet boa.
Quando vc incia um grupo, ele instancia um objeto que "comandara" cara modelo, armazenando-os dentro dele para você poder manipular.
Quando cria um novo modelo, ele inicia um navegador, entra no gpt e já fica pronto pra usar.

https://github.com/user-attachments/assets/260f068a-bd88-4aa8-bd47-e7d431ef8ab1

# exemplo de uso
```python
import asyncio # import asyncio pois é código asincrono
from gpt_selenium.gpt import Modelos, Model # importa Modelos e Model

async def main() -> None: # cria uma função para poder usar livremente o await e o asyncio

  grupo:Modelos = Modelos(debug=False) # antes de tudo, crie um grupo onde ficara armazenado cada modelo, chamando Modelos
  # debug seria o headless, no caso, o False mostra que não queremos que o site apareça 

  model:Model = await grupo.create_model() # aqui criamos o modelo
  # podemos tambem chamar o modelo do grupo, fazendo o seguinte
  # model = grupo.crew[0]
  # quando vc cria um novo modelo, vai direto pra lista dentro de grupo

  while True:
    pergunta = input('perguntar (digite PARAR para encerrar) (digite LIMPAR para limpar o historico):\n')
    if pergunta == 'PARAR':
      break
    elif pergunta == 'LIMPAR':
      await model.clear_history() # no modelo, pode ser usado clear_history onde o site atualiza e então reseta o histórico do modelo
      continue
    
    resp = await model.asq(pergunta) # asq pode ser usado para perguntar algo para o modelo
    print(f'resposta: {resp}')

  await grupo.stop() # tanto para o grupo quanto para o modelo, você pode parar eles

if __name__ == '__main__':
  asyncio.run(main()) # inicia a função main
```
