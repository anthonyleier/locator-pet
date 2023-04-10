# locator-pet

Desenvolvimento de um website com **Django (Python)** com o intuito de localizar animais perdidos. Através do sistema é possível criar posts que ficarão disponíveis para outros usuários visualizarem e entrarem em contato caso tenham alguma informação relevante. O sistema possui **autenticação**, **internacionalização** e utiliza a maioria dos recursos disponíveis do Django, inclusive disponibilizando uma API através do **Django Rest Framework**. Todo o sistema está hospedado no **Google Cloud Plataform**, utilizando **Nginx/Gunicorn** e com banco de dados **PostgreSQL**. Visite o projeto em [https://locatorpet.anthonycruz.com.br](https://locatorpet.anthonycruz.com.br)

<hr>

Development of website in **Django (Python)** for locate lost pets. With the system, its possible to create posts for other users to view and contact if they have any relevant information. The system has **authentication**, **internationalization** and uses most of the Django features, including an API with **Django Rest Framework**. The entire system is hosted on **Google Cloud Plataform**, with **Nginx/Gunicorn** and **PostgreSQL** database. Visit the project at [https://locatorpet.anthonycruz.com.br](https://locatorpet.anthonycruz.com.br)

![locatorpet.anthonycruz.com.br](https://i.imgur.com/BaYO2ck.png)


# Installation

The first step for the installation is to clone the repository. To use this command, you need to specify the URL of the remote repository that you want to clone. Once you execute this command, Git will download all the files and commit history from the remote repository and create a copy on your local machine.

    git clone <URL>

Then you need to install the libraries. When you run this command, pip (which is the package installer for Python) will read the "requirements.txt" file and download and install all the packages listed in it, along with any dependencies that those packages might have.

    pip install -r requirements.txt

The environment variables file must be configured according to the example. In web development, it is common to use environment variables to store sensitive information such as database credentials, API keys, and other configuration settings that should not be publicly visible. The ".env" file is often used to store these environment variables.

    cp .env-example .env

Migrations must be performed to configure the database. The "migrate" command uses a migration history to keep track of the changes made to the database schema. Each migration corresponds to a specific change in the models and contains a set of SQL statements that implement the change.

    python manage.py migrate

In the end, the project can be run with runserver. The "runserver" command starts a lightweight web server that listens for requests on a specified port and IP address. By default, the server runs on port 8000 and listens on all available network interfaces. The server uses the Django application's settings to configure the server.

    python manage.py runserver

Once the development server is running, you can use a web browser to access the application at the specified address and port. Any changes made to the application code or templates will be automatically reloaded by the server, making it easy to test and debug the application.
