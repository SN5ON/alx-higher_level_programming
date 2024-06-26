// fetches and lists the title for all movies by using URL
// movie titles must be list in the HTML tag UL#list_movies

$.get('https://swapi.co/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
