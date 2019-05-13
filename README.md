### How to Use 
#TODO

# Setup database and start server:
```bash
git clone https://github.com/tyler-hitzeman/ping-puma.git
cd ping-puma
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Navigate to http://127.0.0.1:8000/pings/ to verify that the server is running
If so, import the default JSON data (from the `pings/static` directory):

```bash
# Open a separate terminal window (so as not to terminate the server)
# Navigate to the `ping-puma` directory and run the script (under scripts/init_database.py)
python manage.py runscript init_database 
```


Views

Requirements
- django-extensions

### Design Decisions
**Stack**
- Django: I decided to use this framework primarily because I wanted to improve my skills with it. I had used it 
in the past to handle database modeling, but I never created a full app by myself with Django. 
- Python: Using Python was a result of deciding to use Django.
- JavaScript, CSS, jQuery, AJAX, HTML: I enjoy working on the frontend as much as the backend, so adding these 
technologies gave me a good excuse to learn more about them. Some of the features were especially useful in accomplishing simple
tasks that would've taken more work with Django (like sending a simple alert or creating a custom form)  

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

### Process for verifying correctness
I'll address this on a feature-basis:

**Company, Guest, and Ping Models:**
- view in the Django shell or admin page to verify fields were correct and that a user could add a new model
- Django models and forms do a great job validating data, so I let them handle this and simply added some error-handling
in case something went wrong

**Importing models from JSON files:**
- Run script from terminal, then use shell/admin page/view to verify they were created

**Greeting message:**
- send template pings and verify the alert had correct values at different times of day 
(this would've been a great one to unit test, but I did so manually by checking at different parts of day)

**Specifying guest/company for templates:**
- After deciding on representing Guest/Company fields as dropdown forms and foreign keys, I was able to simply
select an option and test sending an alert

**Adding a new template / custom message:**
- Check the shell/admin page/UI to verify the new Ping model was saved
- Check terminal to make sure POST had successful 302 code  

**Generating final message output:**
- For templates: simply reviewing the alert in browser
- For custom pings: viewing the history list contains new ping, and print message in terminal

(I would've loved to apply TDD practices to this project by writing my tests first and having them verify
functionality, but I was worried I wouldn't have enough time to do this.)  

### If Had More Time
- Eliminate all hard-coded values (i.e. urls in templates)
- Make model more flexible so none of the `.json` files would need to be edited before importing
- implemented class-based Views
- Abstract styling and templating to reduce duplication (e.g. when rendering list of pings acrossm ultiple .html files)
- Use Django's `data migration` to import data instead of script
