// Game Difficulty
const EASY = "Easy";
const MEDIUM = "Medium";
const HARD = "Hard";

// Game parameters
var names;

// Create game
function newGame(mode) {
    game.html(game_content);

    loadGameContent();
    document.getElementById("difficulty").innerHTML = mode;

    manual.addClass("disabled");
    new_game.addClass("disabled");
}

// Load game goal and players content
function loadGameContent() {
    getParamValue(score_goal_limit, displayGoalLimit);
    getParamValue(score_names, displayAllPlayers);
}

function displayGoalLimit(value) {
    document.getElementById("goal_limit").innerHTML = value;
}

function displayAllPlayers(value) {
    names = splitNames(value);

    for(i = 0; i < names.length; i++) {
        displayPlayer(i + 1, names[i]);
    }
}

function displayPlayer(index, name) {
    addPlayerDiv(index, name);
}

function addPlayerDiv(index, name) {
    var html = createPlayerDivHTML(index, name);
    $("#player-container").append(html);
}

function createPlayerDivHTML(index, name) {
    var div_id = getPlayerDivID(index);
    var score_id = getPlayerScoreID(index);

    var html = "<li id='" + div_id + "' class='score-item'><div class='score-item-content'>" 
        + name + "</div><img id='equal' src='https://img.icons8.com/ios-filled/50/000000/equal-sign.png'/>"
        + "<div class='score-item-content' id='" + score_id + "'>0</div></li>";

    return html;
}

function getPlayerDivID(index) {
    return "player_" + index;
}

function getPlayerScoreID(index) {
    return "player_" + index + "_score";
}

// Game Control
function startGame() {
    $("#start_game").addClass("disabled");
    $("#pause_game").removeClass("disabled");
}

function pauseGame() {
    $("#start_game").removeClass("disabled");
    $("#pause_game").addClass("disabled");
}

function stopGame() {
    game.html(home_content);
    manual.removeClass("disabled");
    new_game.removeClass("disabled");
}

// Update Score