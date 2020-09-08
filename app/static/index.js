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

var itag;
var file_type;
function update_form_info(ele){
    var $row = ele.closest('tr');
    itag = jQuery('td:nth-child(1)', $row).html();
    file_type = jQuery('td:nth-child(4)', $row).html();
    // these numbers are indexes for the actual table
    convert = $('#convert').val();
    console.log(convert)
    $('#itag').attr('value', itag);
    $('#file_type').attr('value', file_type);
    $('#convert').attr('value', convert)
    

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

    $(document).on('click', '#dl_button', function() { 
        // let myForm = document.getElementById("myForm");
        // let formData = new FormData(myForm);
        // formData.append('itag', itag);
        // formData.append('file_type', file_type);
        // formData.append('convert', convert)

        let download = $.ajax({
            url : '/download',
            type : 'POST',
            data : $('form').serialize(),
            // data : formData,
            // processData: false
        });
        download.done(function(data){
            const url = window.URL.createObjectURL(new Blob([data], {type : 'video/mp4'}));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'file.mp4');
            document.body.appendChild(link);
            alert("HELLO")
            link.click();
            alert("HELLO")
        });

    });

    
    namespace = "/test";
    var socket = io(namespace);
    
    socket.on('message', function(data){
        // alert(data.text);
        $("#loading").text(data.text);
    });

});


// https://r6---sn-8xgp1vo-p5qs.googlevideo.com/videoplayback?expire=1597917301&ei=FfQ9X4OtNo-RhwaLyb6IAg&ip=108.28.114.140&id=o-AKkRTbZTuvBT9TLpYlbsZW_jeAzTVS9asD_hoAWrLqH2&itag=18&source=youtube&requiressl=yes&mh=0V&mm=31%2C29&mn=sn-8xgp1vo-p5qs%2Csn-p5qs7n7z&ms=au%2Crdu&mv=m&mvi=6&pcm2cms=yes&pl=16&gcr=us&initcwndbps=1982500&vprv=1&mime=video%2Fmp4&gir=yes&clen=15593668&ratebypass=yes&dur=187.129&lmt=1574712208345183&mt=1597895610&fvip=6&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgGVegjM-0lY52kGEC1h10iuCMFs_bCieG8n_67JAcSjECIQDtAXacDfx9vWOQ2no0Eb9zDK9uDtFiTZVcDwwIvNxqWQ%3D%3D&sig=AOq0QJ8wRQIgIJwxAN3gNdmky6N8lpu88sHQZnyJ8sI1AncZg0r-hjUCIQDzolhbIinnhbfLQ5KBZqupXUJmU6bMYnTwtviyahcdyA==