// fetches the character name from the URL
// use the JQuery API

$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
