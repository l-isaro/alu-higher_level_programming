-- counts shows by genre

SELECT tv_genres.name AS genre, COUNT(tv_genres.id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_Show_genres ON tv_genres.genre_id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY COUNT(tv_genres.id) DESC;
