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



/*
 *  Backbone.js functions
 */

// add TastypieModel and TastypieCollection (from http://paltman.com/2012/04/30/integration-backbonejs-tastypie/)
window.TastypieModel = Backbone.Model.extend({
    base_url: function() {
        var temp_url = Backbone.Model.prototype.url.call(this);
        return (temp_url.charAt(temp_url.length - 1) == '/' ? temp_url : temp_url+'/');
    },

    url: function() {
        return this.base_url();
    }
});

window.TastypieCollection = Backbone.Collection.extend({
    parse: function(response) {
        this.recent_meta = response.meta || {};
        return response.objects || response;
    }
});


/// Backbone models (extending the above Model and Collection)

// set the API root url for use in Models
var api_root = '/gear/api/v1/'

// GearItem model
var GearItem = TastypieModel.extend({
    url: api_root + 'gearitem'
});

// GearItems collection (all items)
var AllGearItems = TastypieCollection.extend({
    model: GearItem,
    url: api_root + 'gearitem'
});
