window.onload = initall;

function initall(){
    console.log("initall")
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

    var $hidden_eles = ele.closest('td');
    jQuery('input:nth-child(2)', $hidden_eles).val(itag);
    jQuery('input:nth-child(1)', $hidden_eles).val(file_type);
    // the numbers for the nth-child are not in order as they are in tables.py
    // these are the hidden fields, not the fields in the actual table
}