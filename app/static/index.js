window.onload = initall;

function initall(){
    $('#metadata').prop('checked', false);
    $('#convert').prop('checked', false);
}

function onCheckChanged(checked){
    if(checked) {
        $(".dissapear").fadeIn(100, 'linear');
    }else{
        $(".dissapear").fadeOut(100, 'linear');
    }
}

function update_form_info(ele){
    var $row = ele.closest('tr');
    var itag = jQuery('td:nth-child(1)', $row).html();
    var file_type = jQuery('td:nth-child(4)', $row).html();
    // these numbers are indexes for the actual table

    $('#itag').attr('value', itag);
    $('#file_type').attr('value', file_type);

}
$(document).ready(function(){

    $('#submit').click(function(){

        link = $('#link').val();
        $('#loading').html("Loading...");

        req = $.ajax({
            url : '/update',
            type : 'POST',
            data : {
                link : link
            }
        });

        req.done(function(data){
            $('#table').append(data.html);
            $('#loading').text("");

            $('#tn_link').attr('href', link);
            $('#thumbnail').attr('src', data.thumbnail);
            $('#video_title').prepend(data.title);
        });


    });
    console.log("hello");
    namespace = "/test";
    var socket = io(namespace);
    // socket = io.connect('http://' + document.domain + ':' + location.port)

    socket.on('message_from_server', function(data){

        $("#loading").text(data['text']);

        console.log(data["text"]);
        console.log("Helloasdf");
        alert("JHIOOHIJP");

    });
    socket.on('message', function(data){
        alert(data.text);
    });

});

