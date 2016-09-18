### Step 1. Create models
python manage.py inspectdb --database "awdw2012" > awdw2012/models.py
#### Create models on docker container
sudo docker-compose run web python manage.py inspectdb --database "awdw2012" > awdw2012/models.py

Next. Check if every model has PK in place.

### Step 2. Add serializers
python manage.py serializemodels awdw2012 > awdw2012/serializers.py
#### Add serializers on docker container
sudo docker-compose run web python manage.py serializemodels awdw2012 > awdw2012/serializers.py

### Step 3. Add filters
python manage.py addfilters awdw2012 > awdw2012/filters.py
#### Add filters on docker container
sudo docker-compose run web python manage.py addfilters awdw2012 > awdw2012/filters.py

### Step 4. Add views
python manage.py exposeviews awdw2012 > awdw2012/views.py
#### Add views on docker container
sudo docker-compose run web python manage.py exposeviews awdw2012 > awdw2012/views.py

### Step 5. Add urls
python manage.py routeurls awdw2012 > awdw2012/urls.py
#### Add urls on docker container
sudo docker-compose run web python manage.py routeurls awdw2012 > awdw2012/urls.py
