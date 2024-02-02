// Fetch a greeting and display it in the 'hello' element
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
        document.getElementById('hello').textContent = data.hello;
    });
