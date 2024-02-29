$(function() {
    $ .ajax({
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        datatype: "json",
        success: function(data) {
            const movies = data.results;
            const movieList = $("#list_movies")

            $.each(movies, function(i, movie){
                const title = $("<li>").text(movie.title)
                movieList.append(title);
            })
        }
    });
});