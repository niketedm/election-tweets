$(function(){

    $('a[href=#]').click(function(){
        return false
    })

    $('#embeded-tweets').load('/tweets', function(){
        twttr.widgets.load()
        $('#embeded-tweets').children('li').delay(100).animate({
            opacity: 1
        }, 1000)
    })

    $('#more-tweets').bind('click', function(){
        $.get('/tweets?page='+$('#page').val(), function(data){
            $('#embeded-tweets').append(data)
            twttr.widgets.load()
            $('#embeded-tweets').children('li').delay(100).animate({
                opacity: 1
            }, 1000)
        })
        return false;
    })

    $('#back-top').bind('click', function(){
        $('html:not(animated), body:not(animated)').animate({scrollTop: 0 }, 'slow')
    })

})