# Employee Flask API
# This is my API optimize pagination
The base code I used from https://github.com/mtnbarreto/flask-base-api
The data I used from 
## Contents

- [ Optimize API performance](#optimize-api-performance)
- [Commands](#comparision)
## Optimize API performance
- [x] Redis cache
- [x] Use last_id to paginate instead of OFFSET and LIMIT
- [ ] Nginx and Gunicorn
## Comparision
### With Redis Cache
### Without
### Paginate by last_id 
### Paginate by OFFSET and LIMIT (SQLAlchemy paginate library) 
### Without Nginx, Gunicorn 
### With Nginx, Gunicorn 
