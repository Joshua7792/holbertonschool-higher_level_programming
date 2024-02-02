// Use fetch API to get all movie titles and list them
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const movies = data.results;
        const list = document.getElementById('list_movies');
        movies.forEach(movie => {
            const item = document.createElement('li');
            item.textContent = movie.title;
            list.appendChild(item);
        });
    });
