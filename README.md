TEMP - Delete before submitting

### TODO
use Model values to display messages in `ping_templates.html`

Add a greeting variable that changes on time of day

Add sth to avoid running into duplicate key errors when populating JSON
- Drop Guest, Company table after logout?

Run init_databases script if no models
Make models consistent casing (camel vs _s)

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