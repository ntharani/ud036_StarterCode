"""This module creates video objects"""
import webbrowser


class Movie():
    """ Movie Class README
        To access: print(media.Movie.__doc__)
        Please be sure you have python 2.7.1.13+, otherwise there is a known bug
        with webbrowser.open on machines with multiple browsers open.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)