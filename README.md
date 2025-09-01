Curriculo API
Descrição do Projeto
Este é um projeto de desenvolvimento de uma API REST para uma plataforma de currículos, construída com Django e Django REST Framework (DRF). O objetivo é permitir que os usuários criem e gerenciem seus currículos de forma modular, com dados acessíveis e editáveis via API.

Visão Geral e Arquitetura
O projeto foi iniciado seguindo uma arquitetura de monolito bem estruturado. Isso significa que, por enquanto, todos os componentes (dados pessoais, experiência profissional, educação, etc.) residem em uma única aplicação Django, mas estão organizados em "microsserviços" lógicos (as apps do Django), como:

users: Gerenciamento de usuários e autenticação.

personal_data: Dados pessoais do currículo.

professional_experience: Histórico de emprego.

education: Formação acadêmica.

Esta abordagem permite um desenvolvimento mais rápido e a consistência de dados inicial. No futuro, quando a escala e a complexidade justificarem, essas apps poderão ser "cortadas" e transformadas em microsserviços independentes.

Como Começar
Siga os passos abaixo para configurar o projeto e rodar a API localmente.

Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado em sua máquina.

Configuração
Clone o projeto:

git clone [https://github.com/SEU_USUARIO/curriculo-api.git](https://github.com/SEU_USUARIO/curriculo-api.git)
cd curriculo-api

Crie e ative o ambiente virtual (venv):

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

Instale as dependências:

pip install -r requirements.txt

Nota: Como ainda não criamos o arquivo requirements.txt, você pode instalar as dependências manualmente por enquanto:
pip install django djangorestframework psycopg2-binary

Rode o servidor de desenvolvimento:

python manage.py runserver

A API estará disponível em http://127.0.0.1:8000/.

Próximos Passos (Plano de Desenvolvimento)
[ ]  Criar a app users para o modelo de usuário customizado.

[ ]  Criar a app personal_data com os modelos de dados.

[ ]  Desenvolver os serializers e views para a API de dados pessoais.

[ ]  Adicionar as funcionalidades de experiência profissional, educação e habilidades.

[ ]  Configurar a autenticação e permissões da API com DRF.

[ ]  Implementar testes unitários para as funcionalidades críticas.

Contribuição
Sinta-se à vontade para contribuir com ideias, reportar bugs ou enviar Pull Requests. Para isso, crie um novo branch para cada nova funcionalidade.

Licença
MIT License (ou outra licença de sua escolha).