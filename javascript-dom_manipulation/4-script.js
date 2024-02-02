// Add a click event listener to the 'add_item' element to add a new 'li' element to the 'ul' list
document.getElementById('add_item').addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
});
