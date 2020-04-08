// Enable and disable name input
function updateNameInputs(nplayer) {
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

// Update values when input changes
$(document).on('input', '#nplayers', function() {
    updateNameInputs($("#nplayers").val());
})

// Load values on load
function loadGoalInput() {
    $("#ngoals").prop("value", number_goals);
}

function loadPlayerInput() {
    $("#nplayers").prop("value", number_players);
}

function loadNameInput(id, current_name) {
    $(id).prop("placeholder", current_name);
}

window.onload = function() {
    loadGoalInput();
    loadPlayerInput();
    loadNameInput("#name_1", name_1);
    loadNameInput("#name_2", name_2);
    loadNameInput("#name_3", name_3);
    loadNameInput("#name_4", name_4);
    updateNameInputs($("#nplayers").val());
}

// Update storage values on submit
function onSubmit() {
    updateNumberValue(GOAL_STORAGE_NAME,  $("#ngoals").val());
    updateNumberValue(PLAYER_STORAGE_NAME, $("#nplayers").val());
    updateStringValue(NAME_1_STORAGE_NAME, $("#name_1").val());
    updateStringValue(NAME_2_STORAGE_NAME, $("#name_2").val());
    updateStringValue(NAME_3_STORAGE_NAME, $("#name_3").val());
    updateStringValue(NAME_4_STORAGE_NAME, $("#name_4").val());
}

function onReset() {
    localStorage.clear();
}