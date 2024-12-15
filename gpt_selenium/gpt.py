from datetime import datetime, timedelta
import time
from gpt_selenium.navegador import Page

class Model:
    def __init__(self, model:Page) -> None:
        print('modelo gerado')
        self.model:Page = model
        self.ultima_resposta = ''
    
    async def clear_history(self) -> None:
        self.model.driver.refresh()
        time.sleep(2)
    
    async def stop(self) -> None:
        self.model.driver.quit()
        time.sleep(1)
        
    async def asq(self, pergunta:str) -> str:
        if len(pergunta) > 4000:
            pergunta = pergunta[:4000]
        pergunta = pergunta.replace('\n', ' ')
        print(f'\nperguntando: {pergunta}')
        
        self.model.preenche(pergunta, ".//div[contains(@class, 'ProseMirror')]")
        self.model.preenche('\n', ".//div[contains(@class, 'ProseMirror')]")

        last_content = ""
        limite = datetime.now() + timedelta(seconds=30)
        
        while True:
            try:
                if limite < datetime.now():
                    await self.clear_history()
                    return 'modelo não respondeu, reiniciando...'

                try:
                    self.model.espera_aparecer('//*[@href="https://openai.com/policies/usage-policies"]', 1)
                    last_content = 'Não posso responder isso.'
                    break
                except Exception:
                    pass
                
                try:
                    self.model.espera_aparecer('//article[@data-scroll-anchor="true"]')
                    elements = self.model.driver.find_element('xpath', '//article[@data-scroll-anchor="true"]')
                    
                    if elements:
                        content = elements.text
                        time.sleep(1)

                        new_content = self.model.driver.find_element('xpath', '//article[@data-scroll-anchor="true"]').text
                        
                        if content == new_content and 'O ChatGPT disse:\n' in content:
                            content = content.split('O ChatGPT disse:\n')[-1]
                            # if 'ChatGPT' in content or '4o mini' in content or not content:
                            #     continue
                            last_content = content
                            break
                
                    if last_content:
                        break
                
                except Exception as e:
                    print(f"Erro ao encontrar o elemento: {e}")
                    last_content = ""
                    break
            
            except Exception as e:
                print(f"Erro geral: {e}")
                last_content = ""
                break
            
            time.sleep(1)
        
        self.ultima_resposta = last_content
        return last_content

class Modelos:
    def __init__(self, debug:bool=False) -> None:
        self.url:str = 'https://chatgpt.com/'
        self.crew:list[Model] = []
        self.debug:bool = debug
    
    async def stop(self) -> None:
        for model in self.crew:
            try:
                if model:
                    model.stop()
            except:
                print('erro ao finalizar modelo')
        print('todos os modelos foram finalizados')
    
    async def create_model(self) -> Model:
        page:Page = Page(headless=not self.debug)
        page.driver.execute_script("window.open('');")

        page.driver.switch_to.window(page.driver.window_handles[-1])

        page.driver.get('https://chatgpt.com/')
        try:
            page.espera_aparecer('//*[@id="composer-background"]', segundos=5)
        except:
            print('modelo possivelmente não carregou corretamente...')
        
        modelo:Model = Model(page)
        self.crew.append(modelo)
        return modelo