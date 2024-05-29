// adds the class red to the <header> element when the user clicks on the tag
// div#red_header. using the JQuery API

$('div#red_header').click(function () {
    $('header').addClass('red');
  });
