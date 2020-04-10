function displayGoalLimit() {
    $("#ngoals").prop("value", number_goals);
}
function displayPlayerLimit() {
    $("#nplayers").prop("value", number_players);
}
function displayCurrentPlayerName(id, current_name) {
    $(id).prop("placeholder", current_name);
}

function updateEnabledNameInputs(nplayer) {
    for(i = nplayer; i <= MAX_NUMBER_PLAYERS; i++) {
        var id = "#name_" + String(i);
        if(i <= nplayer) {
            $(id).prop("disabled", false);
        }
        else {
            $(id).prop("disabled", true);
        }
    }
}

// Load page with current settings
window.onload = function() {
    displayCurrentGoalLimit();
    displayCurrentPlayerLimit();
    displayCurrentPlayerName("#name_1", name_1);
    displayCurrentPlayerName("#name_2", name_2);
    displayCurrentPlayerName("#name_3", name_3);
    displayCurrentPlayerName("#name_4", name_4);
    updateEnabledNameInputs(Number($("#nplayers").val()));
}

// Update values when input changes
$(document).on('input', '#nplayers', function() {
    updateEnabledNameInputs(Number($("#nplayers").val()));
})

// Update storage values on submit
function onSubmit() {
    updateMotorConfig();
    updateScoreConfig();
}
