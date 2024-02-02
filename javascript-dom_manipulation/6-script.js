// Use fetch API to get the character name and display it
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
        document.getElementById('character').textContent = data.name;
    });
