# Projeto-Resumoflix

## Descrição

Resumoflix é uma plataforma de streaming onde você pode cadastrar filmes e séries, oferecendo aos usuários uma experiência de assistir a resumos de vídeos diretamente do YouTube.

## Desenvolvimento 
O desenvolvimento do Resumoflix foi realizado utilizando várias tecnologias e ferramentas para criar uma aplicação robusta e funcional.

### Backend:

    - Python com Django: A aplicação foi construída usando Django, que fornece um framework completo para desenvolvimento web, incluindo sistema de templates, ORM (Object-Relational Mapping), autenticação, roteamento, e mais.

### Frontend:

    - Bootstrap: Utilizado para estilizar os formulários, garantindo uma interface amigável e responsiva.

    - Tailwind CSS: Aplicado para adicionar classes utilitárias, permitindo um design mais customizável e eficiente.

    - JavaScript: Empregado para adicionar interatividade e melhorar a experiência do usuário.

## Funcionalidades Principais:

    - Autenticação de Usuários: Sistema de cadastro e login para permitir que os usuários acessem a plataforma.

    - Administração de Conteúdos: Interface de administrador para cadastro, edição e remoção de filmes e séries.

    - Exibição de Filmes: Thumbnails que redirecionam para páginas de detalhes dos filmes.

    - Vídeos Embebidos: Reprodução de vídeos de resumos dos filmes e séries diretamente do YouTube.

## Tecnologias utilizadas

[![My Skills](https://skillicons.dev/icons?i=python,django,html,css,tailwind,bootstrap,js)](https://skillicons.dev)

## Como rodar o projeto na sua máquina

### Copie o repositorio
```sh
    git clone https://github.com/Davi504/Projeto-netflix.git
    cd Projeto-netflix

```
### Crie um ambiente virtual

```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### instale as dependencias 

```sh
    pip install -r requirements.txt
```

### realize as migrações do banco de dados

```sh
    python manage.py migrate
```

### crie um super usuario

``` sh
    python manage.py createsuperuser
```

### inicie o servidor 

```sh
    python manage.py runserver
```

### Acesse a aplicação: Abra um navegador e vá para
`http://localhost:8000`