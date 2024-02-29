$ (function () {
    $ .ajax({
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        datatype: "json",
        success: function(data) {
            $("#hello").text(data.hello)
        }
    })
})