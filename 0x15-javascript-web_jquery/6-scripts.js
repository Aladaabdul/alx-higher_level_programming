$(document).ready(function(){
    $("#update_header").click(function(){
        console.log("click")
        $("header").text("New Header!!!");
    });
});