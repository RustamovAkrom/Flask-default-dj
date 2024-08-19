import os
import click
from flask import Flask
from flask_default_dj import utils

APP = None

@click.command("tests")
def tests_command():
    "Run app tests."

    print("It is tests command")
    # import unittest

    # installed_apps = utils.check_installed_apps(APP)

    # for app_name in installed_apps:
    #     import_app = utils.import_string(app_name)
    #     print(import_app.tests)
    #     # if __name__=="__main__":
    #     unittest.main(import_app.tests.__main__)


@click.command("secret_key")
def secret_key_command():
    "Generate secret key."

    print("\n" + "%%"*20 + "\n")
    print(utils.generate_secret_key(max_length=40))
    print("\n" + "%%"*20 + "\n")


@click.command("startproject")
@click.argument("project_name")
def startproject_command(project_name):
    "Create main project."
    
    app_dir = project_name
    try:
        os.makedirs(app_dir)
        os.makedirs(os.path.join(app_dir, "templates", "admin"))
        os.makedirs(os.path.join(app_dir, "templates", "auth"))

        base_dir = os.path.join(os.path.dirname(__file__), "default")
        
        default_project_path = os.path.join(base_dir, "project-cli")

        with open(os.path.join(app_dir, "templates", "admin", "index.html"), "w") as f:
            r = open(os.path.join(default_project_path, "templates", "admin", "index.html-cli"), "r")
            f.write(r.read().replace("<PROJECT_NAME>", project_name))
            r.close()
        
        with open(os.path.join(app_dir, "templates", "auth", "login.html"), "w") as f:
            r = open(os.path.join(default_project_path, "templates", "auth", "login.html-cli"), "r")
            f.write(r.read().replace("<PROJECT_NAME>", project_name))

        with open(os.path.join(app_dir, "templates", "auth", "logout.html"), "w") as f:
            r = open(os.path.join(default_project_path, "templates", "auth", "logout.html-cli"), "r")
            f.write(r.read().replace("<PROJECT_NAME>", project_name))

        with open(os.path.join(app_dir, "__init__.py"), "w") as f:
            r = open(os.path.join(default_project_path, "__init__.py-cli"), "r")
            f.write(r.read().replace("<PROJECT_NAME>", project_name))
            r.close()

        with open(os.path.join(app_dir, "settings.py"), "w") as f:
            r = open(os.path.join(default_project_path, "settings.py-cli"), "r")
            f.write(r.read().replace("<GENERATE_SECRET_KEY>", utils.generate_secret_key()))
            r.close()

        with open(os.path.join(app_dir, "urls.py"), "w") as f:
            r = open(os.path.join(default_project_path, "urls.py-cli"), "r")
            f.write(r.read())

        if not os.path.exists("manage.py"):
            with open("manage.py", "w") as f:
                r = open(os.path.join(base_dir, "manage.py-cli"), "r")
                f.write(r.read().replace("<PROJECT_NAME>", project_name))
                r.close()

        print(f"Successfully creating project configurations.")
    
    except Exception as e:
        print(f"Exceptions on creating project: {e}")
 
    
@click.command("startapp")
@click.argument("app_name")
def startapp_command(app_name):
    "Create new app."

    app_dir = os.path.join("apps", app_name)

    try:
        os.makedirs(app_dir)
        os.makedirs(os.path.join(app_dir, "templates", app_name))
        os.makedirs(os.path.join(app_dir, "static", app_name))

        base_dir = os.path.join(os.path.dirname(__file__), "default")
        default_project_path = os.path.join(base_dir, "app-cli")

        with open(os.path.join(app_dir, "__init__.py"), "w") as f:
            r = open(os.path.join(default_project_path, "__init__.py-cli"), "r")
            f.write(r.read().replace("<APP_NAME>", app_name))
            r.close()

        with open(os.path.join(app_dir, "admin.py"), "w") as f:
            r = open(os.path.join(default_project_path, "admin.py-cli"), "r")
            f.write(r.read().replace("<APP_NAME>", app_name))
            r.close()

        with open(os.path.join(app_dir, "views.py"), "w") as f:
            r = open(os.path.join(default_project_path, "views.py-cli"), "r")
            f.write(r.read().replace("<APP_NAME>", app_name))
            r.close()

        with open(os.path.join(app_dir, "models.py"), "w") as f:
            r = open(os.path.join(default_project_path, "models.py-cli"), "r")
            f.write(r.read().replace("<APP_NAME>", app_name))
            r.close()

        with open(os.path.join(app_dir, "forms.py"), "w") as f:
            r = open(os.path.join(default_project_path, "forms.py-cli"), "r")
            f.write(r.read().replace("<APP_NAME>", app_name))
            r.close()
   
        with open(os.path.join(app_dir, "urls.py"), "w") as f:
            r = open(os.path.join(default_project_path, "urls.py-cli"), "r")
            f.write(r.read().replace("<APP_NAME>", app_name))
            r.close()

        with open(os.path.join(app_dir, "tests.py"), "w") as f:
            r = open(os.path.join(default_project_path, "tests.py-cli"), "r")
            f.write(r.read().replace("<APP_NAME>", app_name))
            r.close()

        print(f"Successfully created app {app_name}.")

    except Exception as e:
        print(f"Exception on createing app: {e}")


@click.command("createsuperuser")
def createsuperuser_command():
    "Create super user."
    def username_input() -> str:
        username = input("Username: ") 

        if username == "":
            print("Username is required !")
            username_input()

        return username

    def password_input() -> str:
        password = input("Password: ") 

        if password == "":
            print("Password is required !")
            password_input()

        return password

    def email_input() -> str:
        email = input("Email: ")

        try:
            if email != "":
                if not len(ls:=email.rsplit("@")) == 2 and ls[1].rsplit(".")[1] in ['ru', 'com', 'nt']:
                    print("Format email are not valid !")
                    email_input()

            return ""
        
        except Exception:
            print("Format email are not valid !")
            email_input()
            
        return email

    username = username_input()
    email = email_input()
    password = password_input()

    from .models import BaseUserModel
    from .extensions import db

    user = BaseUserModel(
        username = username,
        email = email
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)

    print("Successfully created user")


def register_cli_commands(app: Flask):
    global APP
    APP = app

    app.cli.add_command(secret_key_command)
    app.cli.add_command(tests_command)
    app.cli.add_command(startproject_command)
    app.cli.add_command(startapp_command)
    app.cli.add_command(createsuperuser_command)