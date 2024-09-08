# Scrapy_celular

## Passo a Passo Projeto

Criar ambiente virtual
'''pytohn -m venv .venv'''

Ativar ambiente virtual
'''source .venv/Scripts/activate'''

Criar um arquivo .gitignore

Inicializar comandos do git
'''echo "# Scrapy_celular" >> README.md'''
'''git init'''
'''git add README.md'''
'''git commit -m "first commit"'''
'''git branch -M main'''
'''git remote add origin https://github.com/DiogoDanielFerreira/Scrapy_celular.git'''
'''git push -u origin main'''

Fazer web Scraping no site do mercadolivre
'''https://lista.mercadolivre.com.br/celular'''

instalar bibliotecas do scrapy
'''pip install scrapy'''

Criando projeto do scrapy
'''scrapy startproject src'''

Criar spider do site
'''scrapy genspider mercadolivre https://lista.mercadolivre.com.br/celular'''

Iniciar terminal do scrapy
'''scrapy shell'''

Entrando na pagina
'''fetch('https://lista.mercadolivre.com.br/celular')'''

Configurar settings.py para acessar a pagina 
'''USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' '''

Encontrar os blocos padrões

'''reposnse.css('atributo.nome_da_classe')'''

Comando do scrapy para salvar crawlear e salvar arquivo
'''scrapy crawl mercadolivre -o data/data.json'''





