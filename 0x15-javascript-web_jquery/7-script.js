$(function(){
    
    $ .ajax({
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        datatype: "json",
        success: function(data) {
            $("#character").text(data.name)
        }
    });
});