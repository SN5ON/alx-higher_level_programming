// displays the value of hello from that fetch in the HTML tag DIV#hello.
// after fetching from the URl
//

$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
