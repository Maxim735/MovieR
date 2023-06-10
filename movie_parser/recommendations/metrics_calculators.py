import sklearn
import math


class ComputeMetrics:
    @staticmethod
    def compute_genre_similarity(movie1, movie2):
        genres1 = movie1[1:]
        genres2 = movie2[1:]

        return sklearn.metrics.pairwise.cosine_distances(genres1.reshape(1, -1), genres2.reshape(1, -1))

    @staticmethod
    def compute_year_similarity(year1, year2):
        diff = abs(year1[0] - year2[0])
        sim = math.exp(-diff / 10.0)

        return 1 - sim

    @staticmethod
    def compute_distance(x1, x2):
        genre_similarity = ComputeMetrics.compute_genre_similarity(x1, x2)
        year_similarity = ComputeMetrics.compute_year_similarity(x1, x2)

        return genre_similarity * 0.8 + year_similarity * 0.2
