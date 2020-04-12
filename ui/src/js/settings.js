/* ----------------------------------------- */
/* --------------- VARIABLES --------------- */
/* ----------------------------------------- */

var n_players;
var names;

/* ----------------------------------------- */
/* ---------------- ON LOAD ---------------- */
/* ----------------------------------------- */

window.onload = function() {
    getParamValue(score_goal_limit, displayCurrentGoalLimit);
    getParamValue(score_names, displayPlayerRelatedInputs);
    getParamValue(motor_manual_speed, displayCurrentJoystickSpeed);
}

/* ----------------------------------------- */
/* --------------- ON CHANGE --------------- */
/* ----------------------------------------- */

$(document).on('change', '#nplayers', function() {
    if($("#nplayers").val() > n_players) {
        n_players++;
        addPlayerNameDiv(n_players);
        displayCurrentPlayerName(getPlayerInputID(n_players), names[n_players - 1]);
    }
    else if($("#nplayers").val() < n_players) {
        removePlayerNameDiv(n_players);
        n_players--;
    }
})

/* ----------------------------------------- */
/* --------------- ON SUBMIT --------------- */
/* ----------------------------------------- */

function onSubmit() {
    var new_names = createNamesArray(n_players);
    updateScoreConfig(concatenateNames(new_names));
    
    updateMotorConfig();
    alert("Parameters were updated.")
}

/* ----------------------------------------- */
/* ------------- UPDATE INPUTS ------------- */
/* ----------------------------------------- */

function displayCurrentGoalLimit(value) {
    $("#ngoals").prop("value", value);
}

function displayCurrentJoystickSpeed(value) {
    $("#joystick-speed").prop("value", value);
}

function displayPlayerRelatedInputs(value) {
    names = splitNames(value);
    n_players = names.length;

    displayCurrentPlayerLimit(n_players);
    displayAllPlayersNames(n_players, names);
}

function displayCurrentPlayerLimit(value) {
    $("#nplayers").prop("value", value);
}

function displayAllPlayersNames(n_players, names) {
    for(i = 1; i <= n_players; i++) {
        var id = getPlayerInputID(i);

        addPlayerNameDiv(i);
        displayCurrentPlayerName(id, names[i - 1]);
    }
}

function displayCurrentPlayerName(id, value) {
    if(value != undefined) {
        document.getElementById(id).value = value;
    }
}


/* ----------------------------------------- */
/* -------------  NAME INPUTS  ------------- */
/* ----------------------------------------- */

function addPlayerNameDiv(index) {
    var html = createPlayerNameHTML(index);
    $("#name-container").append(html);
}

function createPlayerNameHTML(index) {
    var div_id = getPlayerDivID(index);
    var input_id = getPlayerInputID(index);

    var html = "<div id='" + div_id + "' class='players-names-item'><label>Player " 
            + index + "'s name:</label> <input type='text' id='"
            + input_id + "' pattern='[A-Za-z0-9]{1,15}' required></input></div>";

    return html;
}

function removePlayerNameDiv(index) {
    var id = "#" + getPlayerDivID(index);
    $(id).remove();
}

function getPlayerDivID(index) {
    return "name_" + index;
}

function getPlayerInputID(index) {
    return "name_" + index + "_input";
}

function createNamesArray(n_players) {
    var names = [];
    for(i = 1; i <= n_players; i++) {
        var id = getPlayerInputID(i);
        names[i - 1] = document.getElementById(id).value;
    }
    return names;
}
