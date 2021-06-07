var $add = document.getElementsByClassName('add')[0];
var $form = document.getElementsByClassName('form')[0];

var counter = 2;


$add.addEventListener('click', function(event) {
  var $input = document.createElement('input');
  $input.type = 'text';
  $input.classList.add('id');
  counter += 1;

  $input.name = 't'+ counter;
  $form.insertBefore($input, $add);
});