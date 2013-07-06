$(function(){

    $('a[href=#]').click(function(){
        return false
    })

    $('#embeded-tweets').load('/tweets', function(){
        twttr.widgets.load()
    })

    $('#more-tweets').bind('click', function(){
        $.get('/tweets?page='+$('#page').val(), function(data){
            $('#embeded-tweets').append(data)
            twttr.widgets.load()
        })
        return false;
    })

})