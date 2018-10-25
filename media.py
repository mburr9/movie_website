import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                trailer_youtube):
        '''
        Behavior: contructor used to create space to store movie title,
        storyline, poster image, and youtube trailer
        Inputs: Takes 5 inputs. Self, as well as the movie title, storyline, poster image, and youtube trailer_youtube info
        Outputs: None
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        '''
        Behavior: opens a youtube link with a movie trailer
        Inputs: takes 1 input, self.
        Outputs: None
        '''
        webbrowser.open(self.trailer_youtube_url)
