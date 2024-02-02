// Add a click event listener to update the header text when 'update_header' is clicked
document.getElementById('update_header').addEventListener('click', function() {
  document.querySelector('header').textContent = 'New Header!!!';
});
