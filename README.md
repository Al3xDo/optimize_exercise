# Employee Flask API
# This is my API optimize pagination
The base code I used from https://github.com/mtnbarreto/flask-base-api\
The data I used from https://github.com/datacharmer/test_db
## Contents

- [ Optimize API performance](#optimize-api-performance)
- [Commands](#comparision)
## Optimize API performance
- [x] Redis cache
- [x] Use last_id to paginate instead of OFFSET and LIMIT
- [ ] Nginx and Gunicorn
## Comparision
### With Redis Cache
second call
<img src="https://github.com/Al3xDo/optimize_exercise/blob/develop/docs/images/redis_cache_second_call.png"/>
### Without Redis Cache
second call
<img src="https://github.com/Al3xDo/optimize_exercise/blob/develop/docs/images/last_id.png"/>

### Paginate by last_id
<img src="https://github.com/Al3xDo/optimize_exercise/blob/develop/docs/images/last_id.png"/>

### Paginate by OFFSET and LIMIT (SQLAlchemy paginate library) 

<img src="https://github.com/Al3xDo/optimize_exercise/blob/develop/docs/images/limit_offset.png"/>

### Without Nginx, Gunicorn 
### With Nginx, Gunicorn 
