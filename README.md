
# Movie Recommender

In this project I have created a web app that takes a reference movie as input and returns ten movies as recommendation. All the ten movies are recommended using a machine learning model. 
The other feature of the web app is that it takes a movie name as input and return details likie genres, release date, rating, plot, cast, etc..


## Understanding the approach
So, the first thing is that my project is divided into three parts namely:

-1. Making the ML Model   
-2. Making the web app  
-3. Deploying the web app 

Now let us understand each and every part in detail.
## 1. Making the ML Model
Libraries Used:

-Pandas  
-Numpy  
-Pickle 

Machine Learning Model: 
-Content based filetring: For example, if a user likes to watch movies such as Iron Man, then the recommender system recommends movies of the sci-fi genre or movies of Robert Downy Jr..
-Algorithm: Bag of Words (BoW)  
      
Data files:  
-1. tmdb_5000_credits.csv  
-2. tmdb_5000_movies.csv  
(both files available in the, 'ML Model and Reltd. Files' folder.)

Other concepts used:  
-(i). TEXT VECTORISATION - For plotting each and every movie on a 2-D plane.  
-(ii). COSINE SIMILARITY- For finding the distance of a movie from each and every other movie present in the data set. This way we can take input from user and then find the cosine distance of other movies from it. This way we can get the ten movies that are nearest to our input movie. We need Pickle library to create pickle files of specific functions and then call them in our web app.
## 2. Web App
Libraries Used:  
(i). Pandas  
(ii). Streamlit  
(iii). Pickle  
(iv). Base64  
(v). Requests

Files required to run web app on local host:  
'app.py', 'movie_dict.pkl', 'similarity.pkl' & 'bgf.png'.  

For running the app on local host simply make a project in PyCharm or any other Python IDE of your choice, create a virtual environment, add the above mentioned files into the project folder. Add the libraries to the IDE if they are not pre installed (use pip install command). Then after adding the files and libraries simply open your terminal and give the command, "streamlit run app.py". This command will run the app on local host. Check next section for hosting the website.
## 3. Deployment of Web App
Ones the app is created we need the following files for hosting our web app:  
'app.py', 'movie_dict.pkl', 'similarity.pkl', 'bgf.png', 'requirements.txt'  

Make a GitHub repository and add the above files to it,then simply make an account on Streamlit Cloud and then connect it with your GitHub account. Choose the repository and simply click deploy! And Voila, the app is deployed!
## API References

#### API to fetch the posters of the recommended movies

```http
  https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api key>>&language=en-US
```

| API Provider | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `TMDB` | `composite` | We hit the TMDB API provider with a request that contains movie id and it returns us the poster of the movie.   |

#### API to fetch the poster and details of movie name provided in, "Know Your Next Movie" search bar

```http
  http://www.omdbapi.com/?t={title}&apikey=<<api_key>>
```

| API Provider | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `OMDB`      | `composite and string` | We hit the OMDB API provider with a request that contains movie title and it returns us the poster of the movie and many other details.|



