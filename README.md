# How to Use 

----
### Configure Environment
- [Install official release of Django with pip](https://docs.djangoproject.com/en/2.2/topics/install/#installing-official-release):
- Install django-extensions: `pip install django-extensions` or `pip3 install django-extensions`

### Setup database and start server:
```bash
git clone https://github.com/tyler-hitzeman/ping-puma.git
cd ping-puma
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Import data
Navigate to http://127.0.0.1:8000/pings/ to verify that the server is running.
If so, import the default JSON data (from the `pings/static` directory):

```bash
# Open a separate terminal window (so as not to terminate the server)
# Navigate to the `ping-puma` directory and run the JSON import script (under scripts/init_database.py)

python -W ignore manage.py runscript init_database

# You should see the following terminal output:
#       Company models created
#       Guest models created
#       Ping models created
```

### Follow on-screen instructions from http://127.0.0.1:8000/pings/
Now that the server is running and default data is imported, you should be able to start using the app!


----
# Design Decisions
**Stack**
- Django: I decided to use this framework primarily because I wanted to improve my skills with it. I had used it 
in a past role, but I never created a full app by myself with Django. 
- Python: Using Python was a result of deciding to use Django.
- JavaScript, CSS, Bootstrap, jQuery, AJAX, HTML: I enjoy working on the frontend as much as the backend, so adding these 
technologies gave me a good excuse to learn how to incorporate them into a Django app.
Some of the features were especially useful in 
accomplishing simple tasks that would've taken more work with Django (like sending a simple alert or creating a custom form)  

**Design**
- Templates for views to avoid hard-coded, tightly-coupled URLs
- ModelForm to associate forms with models without duplicating code
- Followed recommendations when organizing project structure (e.g. keeping `middleware`, `static`, `templates` separate)
- Used ForeignKey to represent relationship between Pings and Guests/Company. This worked for this use-case, but I'd 
 make those relationships more flexibile if this were a real application.  

**Other**
- Refer to messages as `pings` in order to avoid naming conflicts with Django
- Removed `id` from .json because Django auto-assigns and id
- Removed `reservation` from .json to facilitate auto-import to Django.
----
