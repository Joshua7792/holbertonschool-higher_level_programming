// Add a click event listener to toggle between 'red' and 'green' classes for the header
document.getElementById('toggle_header').addEventListener('click', function() {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
  } else {
      header.classList.remove('green');
      header.classList.add('red');
  }
});
