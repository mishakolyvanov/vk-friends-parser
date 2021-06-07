var $add = document.getElementsByClassName('add')[0];
var $form = document.getElementsByClassName('form')[0];
$add.addEventListener('click', function(event) {
  var $input = document.createElement('input');
  $input.type = 'text';
  $input.classList.add('id');
  $form.insertBefore($input, $add);
});