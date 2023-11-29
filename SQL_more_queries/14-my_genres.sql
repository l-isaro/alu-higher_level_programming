-- lists all genres of the show Dexter

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_Show_genres ON tv_show_genres.id = tv_genres.id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_Shows.title = 'Dexter'
ORDER BY tv_genres.name
