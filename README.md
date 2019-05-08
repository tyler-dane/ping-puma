TEMP - Delete before submitting

### TODO
**Core Reqirements**
Forms
- Allow user to create custom Pings
- Allow user to pick which Company&Guest to associate with their custom Ping
Views
- Render Ping, Company, and Guests to views
Other
- Add a greeting variable that changes on time of day

Clean up
- Add sth to avoid running into duplicate key errors when populating JSON
    - Drop Guest, Company table after logout?
  
Deploy
- Run init_databases script if no models

#### Making model changes 

- Change your models (in models.py).
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database.
- [Django Doc](https://docs.djangoproject.com/en/2.2/intro/tutorial02/)


**Reminders**
- Need to add model to `admin.py` in order for them to show up in admin site
- accessing shell `python manage.py shell`
- flush db: `python manage.py flush`
    - deletes admin data, too, though. So use `python manage.py createsuperuser`

---
### How to Use
Views

Requirements
- django-extensions

### Design Decisions
**Stack**
- Used Django for practice
- Templates for views to avoid hard-coded, tightly-coupled URLs
- ModelForm to associate forms with models without duplicating code

**Other**
- Refer to messages as `pings` in order to avoid naming conflicts with Django
- Removed `id` from .json because Django auto-assigns and id
- Removed `reservation` from .json to facilitate auto-import to Django.

### If Had More Time
- Eliminate all hard-coded values (i.e. urls in templates)
- Make model more flexible so none of the `.json` files would need to be edited before importing
- Add more error handling
    - (e.g. if user tried making a ping from multiple templates at once)
    - Throwing more specific errors (`ValidationError`) 
- Abstract styling and templating to reduce duplication (e.g. when rendering list of pings acrossm ultiple .html files)
- Use Django's `data migration` to import data instead of script
