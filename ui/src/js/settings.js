var number_of_players = 1;

// Load page with current settings
window.onload = function() {
    getParamValue(score_goal_limit, displayCurrentGoalLimit);
    //getParamValue(score_names, updatePlayerRelatedFormInputs);
    getParamValue(motor_manual_speed, displayCurrentJoystickSpeed);
}

function displayCurrentGoalLimit(value) {
    $("#ngoals").prop("value", value);
}

function displayPlayerRelatedFormInputs(value) {
    var name_array = getNames(value);
    number_of_players = name_array.length;
    displayCurrentPlayerLimit(number_of_players);
}

function displayCurrentPlayerLimit(value) {
    $("#nplayers").prop("value", value);
}

function displayCurrentPlayerName(value, id) {
    $(id).prop("value", value);
}

function displayCurrentJoystickSpeed(value) {
    $("#joystick-speed").prop("value", value);
}

// Update when the number of players changes
$(document).on('change', '#nplayers', function() {
    if($("#nplayers").val() > number_of_players) {
        number_of_players++;
        addPlayerInputName(number_of_players);
    }  
    else if($("#nplayers").val() < number_of_players) {
        removePlayerInputName(number_of_players);
        number_of_players--;
    }
})

// Name input interaction
function addPlayerInputName(index) {
    var html = createPlayerNameHTML(index);
    $("#name-container").append(html);
}

function createPlayerNameHTML(index) {
    var id = "name_" + index;
    var html = "<div id='" + id + "' class='players-names-item'><label>Player " 
    + index + "'s name:</label> <input type='text' id='"+ id +"_input'></input></div>";
    return html;
}

function removePlayerInputName(index) {
    var id = "#name_" + index;
    $(id).remove();
}

// Update dynamic reconfigure values on submit
function onSubmit() {
    updateMotorConfig();
    updateScoreConfig();
    alert("Parameters were updated.")
}