import unittest
from app.models import Movie
# Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test class to test the behavior of the movie class.
    '''

    def setUp(self):
        '''
        set up method that will run before every test.
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','khsjha27hbs',8.5,129993)

    def test_instance(self):
        '''
        checks if self.new_movie is an instance of class Movie.
        '''
        self.assertTrue(isinstance(self.new_movie,Movie))

    def test_init(self):
        '''
        checks if object is instantiated properly.
        '''
        self.assertEqual(self.new_movie.id,1234)
        self.assertEqual(self.new_movie.title,'Python Must Be Crazy')
        self.assertEqual(self.new_movie.overview,'A thrilling new Python Series')
        self.assertEqual(self.new_movie.poster,'https://image.tmdb.org/t/p/w500/khsjha27hbs')
        self.assertEqual(self.new_movie.vote_average,8.5)
        self.assertEqual(self.new_movie.vote_count,129993)






# if __name__ == '__main__':
#     # unittest.main()

#dsf
