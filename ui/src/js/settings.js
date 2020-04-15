/* ----------------------------------------- */
/* --------------- VARIABLES --------------- */
/* ----------------------------------------- */

var nplayers;
var names;

/* ----------------------------------------- */
/* ---------------- ON LOAD ---------------- */
/* ----------------------------------------- */

window.onload = function() {
    getParamValue(score_goal_limit, displayGoalLimit);
    getParamValue(score_names, displayPlayerRelatedInputs);
    getParamValue(motor_manual_speed, displayJoystickLimit);
}

/* ----------------------------------------- */
/* --------------- ON CHANGE --------------- */
/* ----------------------------------------- */

$(document).on('change', '#nplayers', function() {
    while($("#nplayers").val() > nplayers) {
        nplayers++;
        addPlayerDiv(nplayers);
        displayPlayerName(getPlayerInputID(nplayers), names[nplayers - 1]);
    }
    while($("#nplayers").val() < nplayers) {
        removePlayerDiv(nplayers);
        nplayers--;
    }
})

/* ----------------------------------------- */
/* --------------- ON SUBMIT --------------- */
/* ----------------------------------------- */

function updateParameters() {
    var new_names = createNamesArray(nplayers);

    updateScoreConfig(concatenateNames(new_names));
    updateMotorConfig();
    alert("Parameters were updated.")
}

function createNamesArray(nplayers) {
    var names = [];
    for(i = 1; i <= nplayers; i++) {
        var id = getPlayerInputID(i);
        names[i - 1] = document.getElementById(id).value;
    }
    return names;
}

/* ----------------------------------------- */
/* ------------- UPDATE INPUTS ------------- */
/* ----------------------------------------- */

function displayGoalLimit(value) {
    $("#ngoals").prop("value", value);
}

function displayJoystickLimit(value) {
    $("#joystick-limit").prop("value", value);
}

function displayPlayerRelatedInputs(value) {
    names = splitNames(value);
    nplayers = names.length;

    displayPlayerLimit(nplayers);
    displayAllPlayersNames(nplayers, names);
}

function displayPlayerLimit(value) {
    $("#nplayers").prop("value", value);
}

function displayAllPlayersNames(nplayers, names) {
    for(i = 1; i <= nplayers; i++) {
        var id = getPlayerInputID(i);

        addPlayerDiv(i);
        displayPlayerName(id, names[i - 1]);
    }
}

function displayPlayerName(id, value) {
    if(value != undefined) {
        document.getElementById(id).value = value;
    }
}

/* ----------------------------------------- */
/* -------  PLAYER'S DIV INTERACTION  ------ */
/* ----------------------------------------- */

function addPlayerDiv(index) {
    var html = createPlayerDivHTML(index);
    $("#name-container").append(html);
}

function createPlayerDivHTML(index) {
    var div_id = getPlayerDivID(index);
    var input_id = getPlayerInputID(index);

    var html = "<div id='" + div_id + "' class='players-names-item'><label>Player " 
            + index + "'s name:</label> <input type='text' id='"
            + input_id + "' pattern='[A-Za-z0-9]{1,15}' required></input></div>";

    return html;
}

function removePlayerDiv(index) {
    var id = "#" + getPlayerDivID(index);
    $(id).remove();
}

/* ----------------------------------------- */
/* -------------  IDs function  ------------ */
/* ----------------------------------------- */

function getPlayerDivID(index) {
    return "name_" + index;
}

function getPlayerInputID(index) {
    return "name_" + index + "_input";
}