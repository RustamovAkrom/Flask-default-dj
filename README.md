# Flask-Default_DJ

*Quyidagi framework Flask modulini optimizatsiya qilish uchun ishlatilinadi django frameworkiga yaqinlashtirilgan holatda.*

### Ishni boshlash.

**Ishni boshlashdan oldin modulni ozini ornatib olamiz ornatib olamiz.**

```console
$ pip install flask_default_dj
```

**Ornatib bolgandan song proektni ozini ishga tushirishimiz kerak boladi.**

```console
$ flask --app flask_default_dj startproject config
```
*Komandani ishga tushirganizdan keyin sizni direktoriyazda quyidagi papka va fayilar yaratiladi, config.py fayilida asosiy sozlamalar saqlanadi manage.py fayili orqali proektni ishga tushira olasiz.*

```bash
project/
|__manage.py
|__config/
|  |-- __init__.py
|  |-- settings.py
|  |-- urls.py
```

**Proekt yaratib olganizdan song modelarar uchun migratsiya yaratib databasega migratsiyalarni yuborish kerak.**
```console
$ flask --app manage.py db init
```
```console
$ flask --app manage.py migrate -m "initial migrate"
```
```console
$ flask --app manage.py upgrade
```
**Nihoyat proektni ozini ishga tushirsangiz boladi.**
```
& python manage.py
```