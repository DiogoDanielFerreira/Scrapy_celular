# Scrapy_celular

# Passo a Passo Projeto

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


