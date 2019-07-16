-- Lists all the tvshows that have at least a title and a gnere id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres
       WHERE tv_show_genres.show_id = tv_shows.id
       ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
