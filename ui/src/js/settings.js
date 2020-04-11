// Load page with current settings
window.onload = function() {
    getParamValue(score_goal_limit, displayCurrentGoalLimit);
    getParamValue(score_player_limit, updatePlayerRelatedFormInputs);
    getParamValue(score_name_1, displayCurrentPlayerName, "#name_1");
    getParamValue(score_name_2, displayCurrentPlayerName, "#name_2");
    getParamValue(score_name_3, displayCurrentPlayerName, "#name_3");
    getParamValue(score_name_4, displayCurrentPlayerName, "#name_4");
    getParamValue(motor_manual_speed, displayCurrentJoystickSpeed);
}

function displayCurrentGoalLimit(value) {
    $("#ngoals").prop("value", value);
}

function updatePlayerRelatedFormInputs(value) {
    displayCurrentPlayerLimit(value);
    updateEnabledNameInputs(value);
}

function displayCurrentPlayerLimit(value) {
    $("#nplayers").prop("value", value);
}

function updateEnabledNameInputs(nplayer) {
    for(i = 1; i <= MAX_NUMBER_PLAYERS; i++) {
        var id = "#name_" + String(i);
        if(i <= nplayer) {
            $(id).prop("disabled", false);
        }
        else {
            $(id).prop("disabled", true);
        }
    }
}

function displayCurrentPlayerName(value, id) {
    $(id).prop("value", value);
}

function displayCurrentJoystickSpeed(value) {
    $("#joystick-speed").prop("value", value);
}

// Update when the number of players changes
$(document).on('input', '#nplayers', function() {
    updateEnabledNameInputs(Number($("#nplayers").val()));
})

// Update dynamic reconfigure values on submit
function onSubmit() {
    updateMotorConfig();
    updateScoreConfig();
    alert("Parameters were updated.")
}
