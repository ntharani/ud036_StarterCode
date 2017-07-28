import fresh_tomatoes
import media
import tmdbsimple as tmdb

tmdb.API_KEY = '8052964f493a4d5109483f91afe87ef7'

# Pull video data from TMDB.
movie = tmdb.Movies()
popular = movie.popular()["results"] # This in an array of video objects.

# TMDB doesn't provide image URLs. We combine base_url, size and file_path.
# base_url is available from tmdb configuration
cfg = tmdb.Configuration().info()
base_url = cfg['images']['secure_base_url']
size = 'w500' #poster size

def extract_video_details(video):
    # This function creates movie object instances by calling the Movie class and proving it the
    # following attributes from a video object that exists in popular array. The revelant attributes
    #  are id, title and poster_path. It then makes another request to TMBD API to pull in video
    #  details and craft the youtube URL
    first_video = tmdb.Movies(video["id"]).videos()["results"][0]["key"]
    youtube_url = "https://www.youtube.com/watch?v=" + first_video
    return media.Movie(
        video["title"],
        video["overview"],
        base_url+size+video["poster_path"],
        youtube_url)

movies = map(extract_video_details, popular)

fresh_tomatoes.open_movies_page(movies)
# print media.Movie.__doc__
