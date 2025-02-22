# Projeto Resumoflix

## Descrição
Resumoflix é uma plataforma inovadora de streaming onde os usuários podem visualizar resumos de filmes e séries por meio de vídeos embebidos do YouTube. A plataforma foi projetada para fornecer uma experiência amigável e envolvente, permitindo que os administradores cadastrem filmes e séries, enquanto os usuários podem navegar e assistir a resumos desses conteúdos.

## Video da Aplicação Rodando

[Link do video](https://youtu.be/RMMt8hOxD0A?si=xTpQNP9nL_b3aGR1)


### Objetivo
O principal objetivo deste projeto é criar uma plataforma onde os usuários possam facilmente acessar resumos de filmes e séries, ajudando-os a decidir o que assistir de maneira prática e intuitiva.

### Público-alvo
O projeto é destinado a todos os entusiastas de filmes e séries que desejam uma maneira rápida e conveniente de visualizar resumos antes de assistir ao conteúdo completo. Também é útil para administradores que precisam de uma ferramenta eficiente para gerenciar o catálogo de vídeos.

### Futuras Melhorias
- Adicionar funcionalidade de recomendação baseada nos interesses do usuário.
- Implementar comentários e avaliações de usuários para cada vídeo.
- implementar sistema de filtragem por categorias

## Desenvolvimento
O desenvolvimento do Resumoflix foi uma jornada abrangente que envolveu várias etapas, tecnologias e práticas para construir uma plataforma de streaming funcional e robusta. Aqui está uma visão detalhada do processo de desenvolvimento:

### Backend
- **Python com Django**: A aplicação foi construída usando Django, que fornece um framework completo para desenvolvimento web, incluindo sistema de templates, ORM (Object-Relational Mapping), autenticação, roteamento, e mais.

### Frontend
- **Bootstrap**: Utilizado para estilizar os formulários, garantindo uma interface amigável e responsiva.
- **Tailwind CSS**: Aplicado para adicionar classes utilitárias, permitindo um design mais customizável e eficiente.
- **JavaScript**: Empregado para adicionar interatividade e melhorar a experiência do usuário.

## Problemas e Soluções

### Problemas

- **Criação do Carrossel**: Durante a implementação do carrossel, surgiram dificuldades em garantir sua responsividade e funcionamento adequado em diferentes dispositivos.
- **Usuário Personalizado**: A falta de definição de um modelo de usuário personalizado no início do projeto resultou na necessidade de refazer o banco de dados posteriormente.
- **Organização dos Elementos na Tela**: Houve desafios na organização dos elementos na tela para assegurar uma interface limpa e intuitiva para os usuários.
- **Autenticação e Segurança**: Embora a autenticação e segurança tenham sido tranquilas devido às funcionalidades fornecidas pelo Django, algumas personalizações adicionais foram necessárias para atender requisitos específicos.

### Soluções

- **Carrossel Responsivo**: A solução envolveu o uso de frameworks CSS como Bootstrap e Tailwind CSS para criar um carrossel responsivo e funcional em todos os dispositivos.
- **Modelo de Usuário Personalizado**: A implementação do modelo de usuário personalizado exigiu a migração dos dados e a redefinição das relações no banco de dados. Isso foi feito utilizando comandos de migração do Django para minimizar o impacto.
- **Layout e Design**: O uso de Tailwind CSS junto com práticas de design responsivo ajudou na organização dos elementos da tela, proporcionando uma experiência de usuário mais agradável e intuitiva.
- **Personalização da Autenticação**: Adicionamos algumas personalizações à autenticação básica do Django para atender às necessidades do projeto, garantindo segurança e facilidade de uso.

## Funcionalidades Principais
- **Autenticação de Usuários**: Sistema de cadastro e login para permitir que os usuários acessem a plataforma.
- **Administração de Conteúdos**: Interface de administrador para cadastro, edição e remoção de filmes e séries.
- **Exibição de Filmes**: Thumbnails que redirecionam para páginas de detalhes dos filmes.
- **Vídeos Embebidos**: Reprodução de vídeos de resumos dos filmes e séries diretamente do YouTube.

## Tecnologias Utilizadas
[![My Skills](https://skillicons.dev/icons?i=python,django,html,css,tailwind,bootstrap,js)](https://skillicons.dev)

## Como Rodar o Projeto na Sua Máquina

### Copie o repositório

```sh
git clone https://github.com/Davi504/Projeto-Resumoflix.git
cd Projeto-Resumoflix
```

### Crie um ambiente virtual
```sh
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```
### Instale as dependências
```sh
pip install -r requirements.txt
```
### Realize as migrações do banco de dados
```sh
python manage.py make migrations
```
```sh
python manage.py migrate
```

### Crie um super usuário
```sh
python manage.py createsuperuser
```

### Inicie o servidor
```sh
python manage.py runserver
```

### Acesse a aplicação
`Abra um navegador e vá para http://localhost:8000.`

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
