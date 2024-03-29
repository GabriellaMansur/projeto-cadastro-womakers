# Django Web (framework)

* Fundamentos de arquitetura e o padrão MVT
* Ele usa o MVT (Model View Template)
  * Model é a camada de dados, ela define a estrutura do bando de dados
* View lida com a lógica do processamento
  * Template do Django define como o noddos dados serão mostrados para os usuários
* **Diferença entre MTV e MVC**
  * A MVC tem um controller que é responsável por receber e responder as solicitações do usuário. No MVT tem não tem uma camada específica para isso, quem faz esse controle é a view

## Django

* Montar páginas (templates)
* Interagir com diversos bancos de dados (ORM)
* Validar input dos usuários  (forms)
* Controlar acesso (authotization)
* Gerenciar a aplicação (admin)

* **Instalando o ambiente virtual e django**
  * Por que temos que usar o ambiente virtual? Para garantir que os nosso pacotes e intalação vão ser feitas todas localmente, assim vamos ter a garantia que tudo vai ter sido devidamente instalado em uma pasta. Os passos gerais são => instalação, criação e ativação do ambiente  virtual. Posteriormente para o projeto, só é necessário garantir que ele esteja ativado
    * **Instalação:** Entre no terminal no vs code e digite `pip install virtualenv`
    * **Criação:** `python -m venv [nome_do_ambiente]`
    * **Ativação:** entre dentro da pasta criada e digite  `.\Scripts\activate`
    * Depois é só ir em open folder, selecionar a pasta que criamos e abrir
    * Dentro da pasta instale o django usando o comando ``pip install django `
    * Crirar projeto, já dentro da pasta e com o ambiente virtual ativado, `django-admin startproject [nomedoprojeto] .` => aqui onde ficam as configurações gerais
    * Para rodar `python manage.py runserver`, parar  e executar o próximo comando
    * `python manage.py startapp base` => para começar um novo aplicativo
    * O app base é a parte do aplicativo, todas as partes de funcionalidades ficam aqui
    * DEntro de settings, precisamos colocar o 'base' dentro de installed_apps

### Hora de codar

* Rodar o projeto
* Ir ate base > views (são função do python que vão indicar quais funcionalidades vaão existir no nosso sistema e elas vão responder a rotas bem definidas)
  * Todas as telas do nosso sistema representam uma view (elaspodem retonar uma mensagem ou um html)
* Após isso, temos que adicionar a view nas urls

```python
from base.views import inicio
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio)
]
```

### Trabalhando com templates

* Dentro de base crirar a pasta templates e criar o arquivo  html desejado
* Todo css e javascript precisa ficar dentro da pasta static
* Fazer o procedimento de criar a view e a url dessa view
* Para que os recursos que colocamos em static funcionam, precisamos instalar o bootstrao com o comando `pip install django-boostrap-v5`

### Models
* No django, sempre que formos trabalhar com banco de dados, temos que escrever dentro desse arquivo chamado models
* Models são uma abstração que permitem que claase python representem tabelas do banco de dados. Cada classe que definirmos aqui vai representar uma tabela que guarda informações no banco de dados
* Em settins temos que definir qual banco de dados vamos usar, no django já vem o sqlite por padrão
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

* Sempre que mudamos qualquer coisa no banco de dados, temos que rodar esses dois comandos:
```python
python manage.py makemigrations

python manage.py migrate
```
### Filtros, buscas e admin

* Nas URLd dá para ver que o Django já cria uma parte administrativa e com um comando podemos criar um usuário para a parte admnistrativa `python manage.py createsuperuser`

### Djando ORM

* Vamos começar a trabalhar com manipulação em banco de dados, para isso criaremos um novo app com `python manage.py startapp cursos`
* Lembrando que quando criamos algo novo temos que informar nosso projeto, então ir até settings.py e adicioná-lo em instaled apps
* Depois de criado precisamos rodar o comando que vai criar as ligações e que queremos fazer inserções no banco de dados `python  manage.py makemigrations` e depois de criado vamos efetuar de fato essas mudanças com `python manage.py migrate`
* Como queremos que essa parte de crusos também apareça na parte adminstrativa, temos que ir até admin.py e adicionar nossa model

* Agora criamos o app de cadastro de curso. Fezeimos a model, o forms, o template html e usamos a view para ligar esses dois últimos. Mas onde o nosso cadastro de cursos aparacerá? Como o usuário chegará até ele? Para isso teremos que criar um caminho até ele, uma url, uma rota
  * Para isso criaremos um arquivo chamado urls, veja abaixo como ele ficou
```python
from django.urls import path
from cursos.views import criar_curso

app_name = 'Cursos'
urlpatterns = [
    path('criar_curso/', criar_curso, name='criar curso')
]
```

* Recaptulando o que fizemos: criamos uma url para chegar na nossa visualização, essa visualização está fazenod a lógica por trás do criar curso que renderiza os campos do formulário. Formulário que por sua vez importa o que a model está salvando no banco de dados

### Validação de formulários

*


### Utilizando cache na aplicação

* Depois de olhar a documentaçao escolhemos o redis. Para instalar digite `pip install redis`