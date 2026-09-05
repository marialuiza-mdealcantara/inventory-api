# Development Log — Inventory App

## Módulo 02 — Ambiente

### Parte 1 — Ambiente Windows, Git/GitHub e preparação inicial do Backend

**Status:** Concluída

**Objetivo:**
Preparar o ambiente principal de desenvolvimento no Windows, estabelecer o versionamento do projeto e criar a base inicial do backend Python + FastAPI.

---

## 1. Ambiente de desenvolvimento

O ambiente principal utilizado nesta etapa é:

- Sistema operacional: Windows
- Editor/IDE: Visual Studio Code
- Terminal: PowerShell
- Linguagem do backend: Python
- Framework da API: FastAPI

O desenvolvimento iOS será realizado posteriormente em ambiente Mac utilizando Xcode.

---

## 2. Ferramentas verificadas

Durante a preparação do ambiente foram verificadas as principais ferramentas utilizadas nesta etapa.

Versões observadas:

- Python 3.14.7
- pip 26.2.1
- Git 2.53.0.windows.1
- Visual Studio Code 1.135.0

Também foi criado e configurado um ambiente virtual Python para o projeto.

---

## 3. Repositório do projeto

O projeto backend foi criado com o nome:

`inventory-api`

Localmente:

`C:\Users\maria\Projetos\inventory-api`

O repositório Git foi inicializado e a branch principal foi definida como `main`.

O repositório remoto foi configurado no GitHub.

---

## 4. Git e versionamento

Foram realizadas, entre outras, as seguintes operações durante a preparação:

```text
git init
git branch -M main
git config --global user.name
git config --global user.email
git remote add origin
git add .
git commit
git push
```

Primeiro commit:

```text
c2e3743
chore: inicializa estrutura do projeto
```

O commit foi enviado ao repositório remoto com sucesso e a branch local `main` passou a acompanhar `origin/main`.

---

## 5. Estrutura inicial do backend

A estrutura criada nesta etapa foi:

```text
inventory-api/
├── .venv/
├── app/
│   └── main.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

Essa estrutura representa a preparação inicial do backend realizada na Parte 1.

As camadas internas previstas pela arquitetura, como `routes/`, `schemas/`, `services/`, `repositories/`, `integrations/`, `core/` e `utils/`, ainda não foram implementadas como estrutura funcional nesta etapa. Elas serão introduzidas posteriormente conforme a evolução do sistema e os módulos correspondentes.

---

## 6. Ambiente virtual

Foi criado o ambiente virtual:

`.venv`

O ambiente foi ativado no terminal e identificado pelo prefixo `(.venv)`.

O VS Code também foi configurado para utilizar o interpretador Python associado ao ambiente virtual do projeto.

---

## 7. Dependências iniciais

Foram instaladas as dependências necessárias para a execução inicial da API, incluindo:

- FastAPI
- Uvicorn

As dependências instaladas foram registradas no arquivo `requirements.txt` utilizando o ambiente virtual do projeto.

---

## 8. Aplicação FastAPI inicial

Foi criado o arquivo:

`app/main.py`

A aplicação inicial contém a configuração básica do FastAPI e um endpoint inicial:

```http
GET /
```

O endpoint retorna uma mensagem simples de confirmação de funcionamento da API.

---

## 9. Execução local

A aplicação foi executada utilizando:

```text
uvicorn app.main:app --reload
```

O servidor iniciou corretamente em:

`http://127.0.0.1:8000`

O terminal apresentou a mensagem de inicialização concluída:

```text
Application startup complete.
```

---

## 10. Swagger

A documentação automática da API foi acessada em:

`http://127.0.0.1:8000/docs`

A interface Swagger foi carregada corretamente e apresentou a aplicação `Inventory API` e o endpoint inicial `GET /`.

---

## 11. Validação

A Parte 1 foi validada pelos resultados observados durante a execução do ambiente e da aplicação.

Foram confirmados:

- ferramentas principais disponíveis no Windows;
- ambiente virtual criado e ativado;
- interpretador Python do projeto selecionado no VS Code;
- FastAPI instalado;
- Uvicorn instalado;
- aplicação FastAPI iniciando localmente;
- documentação Swagger acessível;
- endpoint inicial `GET /` respondendo com HTTP `200 OK`;
- repositório Git criado e sincronizado com o GitHub.

A evidência prática dessas validações foi obtida pelos comandos executados no PowerShell, pela estrutura observada no VS Code e pelos resultados apresentados no terminal e no navegador.

---

## 12. Limites desta etapa

A Parte 1 não implementou as funcionalidades de negócio do sistema.

Não foram implementados nesta etapa:

- `/health`;
- schemas de negócio;
- Pydantic aplicado aos contratos funcionais do sistema;
- CRUD de produtos;
- persistência em `produtos.json`;
- persistência em `dominios.json`;
- repositories funcionais;
- integração com Google Drive;
- autenticação;
- upload de imagens;
- regras de negócio de categorias, estados e plataformas;
- integração com o aplicativo iOS.

O objetivo desta etapa foi preparar e validar a base inicial do ambiente e do backend.

---

## 13. Relação com o Módulo 03

O trabalho realizado até aqui constitui a base inicial para o desenvolvimento posterior da API.

O Módulo 03 será responsável pelo desenvolvimento efetivo da API FastAPI, incluindo o endpoint `/health`, schemas, respostas HTTP e os conceitos de HTTP, REST, requests, responses, status codes e Pydantic.

Neste momento, o M03 deve ser considerado **apenas iniciado em sua base inicial**, devido à criação e execução da aplicação FastAPI e do endpoint `GET /`.

Nenhuma funcionalidade adicional do M03 foi desenvolvida como parte deste encerramento.

---

## 14. Estado da M02 — Parte 1

```text
M02 — Parte 1
│
├── ✅ M02.1 — Verificar ferramentas
├── ✅ M02.2 — Git + GitHub
├── ✅ M02.3 — Estrutura inicial do Backend
├── ✅ Validação do Backend
└── ✅ Documentação formal da Parte 1
```

A Parte 1 do Módulo 02 está encerrada.

---

## 15. Pendências da M02 — Parte 2

As seguintes atividades permanecem pendentes e serão realizadas posteriormente no ambiente Mac:

```text
M02.4 — Preparar ambiente Swift
M02.5 — Estrutura inicial do projeto iOS
M02.6 — Preparar ambiente iOS
Execução local do projeto iOS
Validação do projeto iOS
Documentação da Parte 2
```

Essas atividades não foram executadas nem validadas durante a Parte 1 e não devem ser consideradas concluídas antecipadamente.

---

## 16. Estado geral do Módulo 02

```text
M02 — Ambiente
│
├── Parte 1 — Windows, Git/GitHub e Backend
│   └── ✅ Concluída
│
└── Parte 2 — Ambiente iOS
    └── 🔴 Pendente para execução no Mac
```

O Módulo 02 completo permanece pendente até a realização e validação da Parte 2.

---

## 17. Próximo marco

O próximo trabalho será a execução da Parte 2 do Módulo 02 no ambiente Mac:

```text
M02 — Parte 2
↓
Ambiente Mac
↓
Swift
↓
SwiftUI
↓
Xcode
↓
Projeto iOS
↓
Execução local
↓
Validação
↓
Documentação
↓
Conclusão formal do M02
```

Somente após a conclusão formal do Módulo 02 será retomado o desenvolvimento do Módulo 03 — FastAPI.
