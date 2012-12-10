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


// refresh an individual item in the view, provided with the right data (get from an AJAX request or some javascript object)
function refill_item(id, item){
    // generate new item
    var new_item_html = ich.gear_item(item).hide();
    // fade the old item out, and begin the callback to replace the old item with the new
    $("#gear_"+id).fadeOut(166, function() {
        $(this).replaceWith(new_item_html);
        // fade the new item in (need to re-call with id because the old object has been deleted by replaceWith() )
        $("#gear_"+id).fadeIn(166);
    });
};


// refresh an individual item with an AJAX request and the above refill_item()
function refresh_item(id){
    // get the new item from the Dajaxice function, refill the item in the callback
    Dajaxice.chicago.gear.get_item(function(data){
        refill_item(id, data.items[0]);
    }, 
    // and pass the id to Dajaxice
    {"id":id});
};


//
// Mustache / ICanHaz templates
//

// basic table for showing gear items
// ich.addTemplate('gear_table', '<div class="table-wrapper"><table id="gear_table"><thead><tr><th>Item</th><th>Description</th><th>Weight</th><th>Status</th><th></th></tr></thead><tbody></tbody></table></div>')
// template for new items in table
// ich.addTemplate('gear_item', '<tr class="{{ status }}"><th>{{ model }} ({{ make }})</th><td>{{ description }}</td><td>{{ weight }}</td><td>{{ status }}</td><td>Action</td></tr>')


