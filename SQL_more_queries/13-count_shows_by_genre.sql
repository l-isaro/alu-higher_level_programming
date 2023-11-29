-- counts shows by genre

SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
INNER JOIN  tv_Shows ON tv_genres.genre_id = tv_genres.id
ORDER BY COUNT(tv_shows.id)
GROUP BY tv_genres.name
