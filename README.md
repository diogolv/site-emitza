# Emitza - Soluções em Tecnologia e Inovação

Este repositório contém o código-fonte do site institucional da Emitza, uma empresa fictícia focada em soluções tecnológicas personalizadas para pequenas e médias empresas. O projeto foi desenvolvido utilizando o framework web Django e implantado em um ambiente de produção completo no Ubuntu.

## 🚀 Tecnologias Utilizadas

* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Python 3.x, Django 5.x
* **Banco de Dados:** PostgreSQL
* **Servidor Web:** Nginx
* **Servidor de Aplicação:** Gunicorn
* **Gerenciamento de Dependências:** `pip` (com `venv` para isolamento de ambiente)
* **Controle de Versão:** Git / GitHub
* **CDN/Segurança:** Cloudflare

## ✨ Funcionalidades Principais

* **Página Inicial (Landing Page):** Design moderno e responsivo, destacando os serviços e diferenciais da Emitza.
* **Responsividade:** Layout adaptável para dispositivos móveis, tablets e desktops.
* **Formulário de Contato:** Para comunicação direta com a equipe. (Se você tiver um)
* **Área do Cliente (Login):** Autenticação de usuários com sistema de segurança CSRF implementado.
* **Administração:** Painel administrativo do Django para gerenciamento de conteúdo e usuários.

## 🛠️ Configuração e Implantação

Este projeto foi configurado para ser executado em um ambiente de produção Linux (Ubuntu Server) com Nginx para servir arquivos estáticos e proxy reverso para o Gunicorn, que gerencia a aplicação Django. O banco de dados PostgreSQL é utilizado para armazenamento de dados.

### Pré-requisitos

* Python 3.x
* PostgreSQL
* `venv` (ambiente virtual Python)
* Git
* Nginx
* Gunicorn

### Passos para Configuração (Exemplo simplificado)

1.  **Clonar o Repositório:**
    ```bash
    git clone [https://github.com/diogolv/site_emitza.git](https://github.com/diogolv/site-emitza.git)
    cd Emitza
    ```
2.  **Configurar Ambiente Virtual e Dependências:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Configurar Banco de Dados (PostgreSQL):**
    * Criar banco de dados e usuário no PostgreSQL.
    * Atualizar `settings.py` com as credenciais do banco.
4.  **Aplicar Migrações:**
    ```bash
    python manage.py migrate
    ```
5.  **Criar Superusuário:**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Coletar Arquivos Estáticos:**
    ```bash
    python manage.py collectstatic --noinput
    ```
7.  **Configurar Gunicorn e Nginx:**
    * Criar e configurar serviços Gunicorn para a aplicação Django.
    * Configurar Nginx como proxy reverso para Gunicorn e para servir arquivos estáticos.
8.  **Reiniciar Serviços:**
    ```bash
    sudo systemctl restart gunicorn
    sudo systemctl restart nginx
    ```

## 🌐 Acesso ao Site

O site está disponível em: [https://emitza.com](https://emitza.com)

## 🤝 Contribuições

Contribuições são bem-vindas\! Para contribuir, por favor, siga os seguintes passos:

1.  Faça um fork do projeto.
2.  Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`).
3.  Faça suas mudanças e commit (`git commit -m 'Add some AmazingFeature'`).
4.  Faça push para a branch (`git push origin feature/AmazingFeature`).
5.  Abra um Pull Request.

---

**Desenvolvido por:** [Diogo]