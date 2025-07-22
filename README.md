
# How to run
```bash
python -m venv ./venv
source .venv/bin/activate
pip3 install -r requrements.txt
python manage.py migrate
python manage.py runserver
```
-------

# Create short url

````
POST http://127.0.0.1:8000/shorter/

BODY 
{
    "original_url": "https://www.google.com/business/?subid=ww-ww-et-g-awa-a-g_hpbfoot1_1!o2&utm_source=google.com&utm_medium=referral&utm_campaign=google_hpbfooter&fg=1"
}

Response
{
    "original_url": "https://www.google.com/business/?subid=ww-ww-et-g-awa-a-g_hpbfoot1_1!o2&utm_source=google.com&utm_medium=referral&utm_campaign=google_hpbfooter&fg=1",
    "short_url": "http://127.0.0.1:8000/shorter/d57da9121f713c1cdbc29519264b22b1/"
}

````

--------

# Get original url

```
GET http://127.0.0.1:8000/shorter/d57da9121f713c1cdbc29519264b22b1/

Response
{
    "original_url": "https://www.google.com/business/?subid=ww-ww-et-g-awa-a-g_hpbfoot1_1!o2&utm_source=google.com&utm_medium=referral&utm_campaign=google_hpbfooter&fg=1",
    "short_url": "http://127.0.0.1:8000/shorter/d57da9121f713c1cdbc29519264b22b1/"
}

```