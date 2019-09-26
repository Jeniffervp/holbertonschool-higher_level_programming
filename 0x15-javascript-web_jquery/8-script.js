$.get('https://swapi.co/api/films/?format=json', function (data) {
  for (const t of data.results) {
    $('UL#list_movies').append('<li>' + t.title + '</li>');
  }
});
