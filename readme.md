# locator-pet

Desenvolvimento de um website com **Django (Python)** com o intuito de localizar animais perdidos. Através do sistema é possível criar posts que ficarão disponíveis para outros usuários visualizarem e entrarem em contato caso tenham alguma informação relevante. O sistema possui **autenticação**, **internacionalização** e utiliza a maioria dos recursos disponíveis do Django, inclusive disponibilizando uma API através do **Django Rest Framework**. Todo o sistema está hospedado no **Google Cloud Plataform**, utilizando **Nginx/Gunicorn** e com banco de dados **PostgreSQL**. Visite o projeto em [https://locatorpet.anthonycruz.com.br](https://locatorpet.anthonycruz.com.br)

<hr>

Development of website in **Django (Python)** for locate lost pets. With the system, its possible to create posts for other users to view and contact if they have any relevant information. The system has **authentication**, **internationalization** and uses most of the Django features, including an API with **Django Rest Framework**. The entire system is hosted on **Google Cloud Plataform**, with **Nginx/Gunicorn** and **PostgreSQL** database. Visit the project at [https://locatorpet.anthonycruz.com.br](https://locatorpet.anthonycruz.com.br)


# Installation

The first step for the installation is to clone the repository.

    git clone <URL>

Then you need to install the libraries.

    pip install -r requirements.txt

The environment variables file must be configured according to the example.

    cp .env-example .env

Migrations must be performed to configure the database.

    python manage.py migrate

In the end, the project can be run with runserver.

    python manage.py runserver
