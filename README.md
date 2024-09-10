# Scrapy_celular

## Passo a Passo Projeto

Criar ambiente virtual
'''bash
pytohn -m venv .venv
'''

Ativar ambiente virtual
'''bash
source .venv/Scripts/activate
'''

Criar um arquivo .gitignore

Inicializar comandos do git
''' bash
echo "# Scrapy_celular" >> README.md
'''

''' bash
git init
'''

''' bash
git add README.md
'''

''' bash
git commit -m "first commit
"'''

''' bash
git branch -M main
'''

''' bash
git remote add origin https://github.com/DiogoDanielFerreira/Scrapy_celular.git
'''

''' bash
git push -u origin main
'''

Fazer web Scraping no site do mercadolivre
'''https://lista.mercadolivre.com.br/celular'''

instalar bibliotecas do scrapy
''' bash
pip install scrapy
'''

Criando projeto do scrapy
''' bash
scrapy startproject src
'''

Criar spider do site
''' bash
scrapy genspider mercadolivre https://lista.mercadolivre.com.br/celular
'''

Iniciar terminal do scrapy
''' bash
scrapy shell
'''

Entrando na pagina
''' bash
fetch('https://lista.mercadolivre.com.br/celular')
'''

Configurar settings.py para acessar a pagina 
''' bash
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
'''

Encontrar os blocos padrões

''' bash
reposnse.css('atributo.nome_da_classe')
'''

Comando do scrapy para salvar crawlear e salvar arquivo

''' bash
scrapy crawl mercadolivre -o data/data.json
'''

Para conseguir crawlear as 10 paginas precisa mudar: ROBOTSTXT_OBEY = False

Para criar banco de dados entre na pasta src e rode o comando

''' bash
python transformacao/main.py
'''

Para visualizar o dash entre na pasta src e rode o comando 

''' bash
streamlit run dashboard/app.py
''' 




