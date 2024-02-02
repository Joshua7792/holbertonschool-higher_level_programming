// Add a click event listener to the element with id 'red_header' to add 'red' class to the header
document.getElementById('red_header').addEventListener('click', function() {
  document.querySelector('header').classList.add('red');
});
