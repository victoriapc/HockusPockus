// Game Parameters Constants 
const MAX_NUMBER_GOALS = 10;
const DEFAULT_NUMBER_GOALS = 5;
const MAX_NUMBER_PLAYERS = 4;
const DEFAULT_NUMBER_PLAYERS = 1;

const GOAL_STORAGE_NAME = "ngoal";
const PLAYER_STORAGE_NAME = "nplayer";

const DEFAULT_NAME_1 = "Blue";
const DEFAULT_NAME_2 = "Red";
const DEFAULT_NAME_3 = "Green";
const DEFAULT_NAME_4 = "Yellow";

const NAME_1_STORAGE_NAME = "name_1";
const NAME_2_STORAGE_NAME = "name_2";
const NAME_3_STORAGE_NAME = "name_3";
const NAME_4_STORAGE_NAME = "name_4";

// Current values variables
var number_goals = null;
var number_players = null;

var name_1 = null;
var name_2 = null;
var name_3 = null;
var name_4 = null;

// Loading number of goals and number of players
function loadNumberValue(param, default_value, reset) {
    var current = Number(localStorage.getItem(param));
    if(current == null || current == 0 || !(Number.isInteger(current))) {
        console.log("HEY");
        current = default_value;
        localStorage.setItem(param, default_value);
    }
    return current;
}

// Loading name of players
function loadStringValue(param, default_value) {
    var current = localStorage.getItem(param);
    if(current == null || current.length == 0) {
        current = default_value;
        localStorage.setItem(param, default_value);
    }
    return current;
}

// Update value in storage system
function updateNumberValue(param, value) {
    localStorage.setItem(param, value);
}

function updateStringValue(param, value) {
    if(value.length != 0) {
        localStorage.setItem(param, value);
    }
}

// Load values
number_goals = loadNumberValue(GOAL_STORAGE_NAME, DEFAULT_NUMBER_GOALS);
number_players = loadNumberValue(PLAYER_STORAGE_NAME, DEFAULT_NUMBER_PLAYERS);
name_1 = loadStringValue(NAME_1_STORAGE_NAME, DEFAULT_NAME_1);
name_2 = loadStringValue(NAME_2_STORAGE_NAME, DEFAULT_NAME_2);
name_3 = loadStringValue(NAME_3_STORAGE_NAME, DEFAULT_NAME_3);
name_4 = loadStringValue(NAME_4_STORAGE_NAME, DEFAULT_NAME_4);