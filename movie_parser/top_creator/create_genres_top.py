class TopCreator:
    @staticmethod
    def _get_top_by_rating(data, rating_type, percentile=0.2):
        """
        Weighted Rating (WR) = (v/(v+m)R)+(m/(v+m)C)
        """
        votes_amount = data['votes ' + rating_type]
        average_rating = data['rating ' + rating_type]

        vote_counts = data.loc[data['votes ' + rating_type].notnull(), 'votes ' + rating_type].astype('int')
        vote_avg = data.loc[data['rating ' + rating_type].notnull(), 'rating ' + rating_type].astype('float32')
        minimum_votes = vote_counts.quantile(percentile)
        mean_vote = vote_avg.mean()

        qualified = data.loc[(data['votes ' + rating_type] > minimum_votes)]

        qualified['rating'] = 0
        qualified['rating'] = votes_amount / (votes_amount + minimum_votes) * average_rating +\
            minimum_votes / (votes_amount + minimum_votes) * mean_vote
        qualified = qualified.sort_values('rating', ascending=False).head(300)

        return qualified

    @classmethod
    def get_genre_top(cls, data, genre, content_type, rating_type):
        data = data[(data['is_' + genre] == 1) & (data['type'] == content_type)]
        return cls._get_top_by_rating(data, rating_type=rating_type)

    @classmethod
    def get_country_top(cls, data, country, content_type, rating_type):
        data = data[(data['from_' + country] == 1) & (data['type'] == content_type)]
        return cls._get_top_by_rating(data, rating_type=rating_type)

    @classmethod
    def get_genre_no_mix_top(cls, data, content_type, lovely_genre, unloved_genre, rating_type):
        data = data[(data['is_' + lovely_genre] == 1) & (data['is_' + unloved_genre] == 0) &
                    (data['type'] == content_type)]
        return cls._get_top_by_rating(data, rating_type=rating_type)

    @classmethod
    def get_year_top(cls, data, year, rating_type, content_type):
        data = data[(data['year'] == year) & (data['type'] == content_type)]
        return cls._get_top_by_rating(data, rating_type=rating_type)
