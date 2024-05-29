// adds a <li> element to a list when the user clicks on the tag DIV#add_item
// new element must be: <li>Item</li> added to UL.my_list

$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
