/*
 * javascript library for gear app
 */

function ajax_login_callback(data){
    if (data.status == 'Success!'){
        $('#login_errors').html('');
        $('#login_form_wrapper').html("Successfully logged in.  Taking you to your homepage...");
        setTimeout(function() {
            window.location.href = "/";
        }, 2000);
    }else{
        $('#login_errors').html('');
        for (message in data){
            $('#login_errors').append("<p class='error'>" + message + ": " + data[message][0] + "</p>");
        }
    }
};

function ajax_login(){
    data = $("#login_form").serializeObject();
    Dajaxice.chicago.gear.login(ajax_login_callback, {'form':data});
};

// Login form - tie enter key to button (fires JS, not 'submit' event)
$("#login_form").keyup(function(event){
    if(event.keyCode == 13){
        $("#login_button").click();
    }
});


// handle the output of calling the Dajaxice all_items
function populate_all_gear_callback(data){
    if (data.items.length !== 0) {
        // first, clear the placeholder and start up a table:
        $('#all_gear').html(ich.gear_table());
        // then append each item as items in the table
        for (item in data.items){
            $('#gear_table').append(ich.gear_item(data.items[item]));
        }
    }else{
        $('#all_gear').html('<p>No gear found.</p>');
    }
};

function populate_all_gear(){
    Dajaxice.chicago.gear.all_items(populate_all_gear_callback);
};


// 


//
// Mustache / ICanHaz templates
//

// basic table for showing gear items
// ich.addTemplate('gear_table', '<div class="table-wrapper"><table id="gear_table"><thead><tr><th>Item</th><th>Description</th><th>Weight</th><th>Status</th><th></th></tr></thead><tbody></tbody></table></div>')
// template for new items in table
// ich.addTemplate('gear_item', '<tr class="{{ status }}"><th>{{ model }} ({{ make }})</th><td>{{ description }}</td><td>{{ weight }}</td><td>{{ status }}</td><td>Action</td></tr>')


