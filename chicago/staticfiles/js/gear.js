/*
 * javascript library for gear app
 */

function ajax_login_callback(data){
    console.log('received data:');
    console.log(data);
    if (data.status == 'Success!'){
        $('#login_errors').html('');
        $('#login_form_wrapper').html("Successfully logged in.  Taking you to your homepage...");
        setTimeout(function() {
            window.location.href = "/";
        }, 2000);
    }else{
        $('#login_errors').html('');
        for (message in data){
            console.log(message);
            $('#login_errors').append("<p class='error'>" + message + ": " + data[message][0] + "</p>");
        }
    }
};

function ajax_login(){
    data = $("#login_form").serializeObject();
    console.log('sending data...');
    console.log(data);
    Dajaxice.chicago.gear.login(ajax_login_callback, {'form':data});
};

// Login form - tie enter key to button (fires JS, not 'submit' event)
$("#login_form").keyup(function(event){
    if(event.keyCode == 13){
        $("#login_button").click();
    }
});
