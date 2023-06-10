# Movier - web API for movie analytics and recommendations

**Technologies:**
- Python 3.11
- FastAPI for web API
- Sklearn for recommendations
- pyngrok

The data for the project was taken from the open API of Kinopoisk and an open competition on the Kaggle platform. They are coming in json format was converted into a csv table and processed.
The processing of key queries was written using the FastAPI framework.
**Pyngrok** - Python client for convenient use of the ngrok service, which provides a public address for your local web server, forwarding all requests to your computer through your Internet channel.
**Pyngrok** provides a simple interface for configuring and running an ngrok tunnel, as well as for managing a list of active tunnels. Working with Pyngrok, you can run ngrok tunnels and get public URLs, configure a proxy server, log requests, and much more.

**Implemented requests:**

Requests connected **with users**:
- /register/ register user by username and email. Returns unique user id
- /review/like/user/ post rating for movie by its id
- /review/delete/user/ delete user review by user id

Requests connected **with recommendations**:
- /recommendations/user/{user_id} get personal recommendations by user id. Recs are being created by user reviews
- /recommendations/content/genres/{movie_title} get content recommendations by movie. Recs are being created by movie genres
- /recommendations/content/years/{movie_title} get content recommendations by movie. Recs are being created by movie year
- /recommendations/content/{movie_title} get mixed content recommendations by movie. Recs are being created by year(weight 0.2) and genres(weight 0.8)

Requests connected **with charts**:
- /charts/countries/{country}/{content_type}/{rating_type}/{amount} get top movies by country
- /charts/genres/{genre}/{content_type}/{rating_type}/{amount} get top movies by genre
- /charts/years/{year}/{content_type}/{rating_type}/{amount} get top movies by year
- 

Requests connected **with data**:
- /data/year/{movie_name} get year of the movie by name
- /data/genres/{movie_name} get genres of the movie by name
- /data/countries/{movie_name} get country of the movie by name
- /data/description/{movie_name} get description of the movie by name
- /data/ratings/{movie_name} get ratings of the movie by name
- /data/movie_type/{movie_name} get type of the movie by name
- /data/movie_length/{movie_name} get length of the movie by name
- /data/update/{data_amount} update data from Kinopoisk
