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
- Used Django for practice
- Used templates for views to avoid hard-coded, tightly-coupled URLs
- Removed `id` from .json because Django auto-assigns and id
- Removed `reservation` from .json to facilitate auto-import to Django. Would allow for this if I dedicated more time