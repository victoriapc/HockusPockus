// Difficulty
function easy() {
    newGame(EASY);
    document.getElementById("difficulty").innerHTML = "Easy";
}

function medium() {
    newGame(MEDIUM);
    document.getElementById("difficulty").innerHTML = "Medium";
}

function hard() {
    newGame(HARD);
    document.getElementById("difficulty").innerHTML = "Hard";
}

// Show Game Content
function newGame(mode) {
    game.html(game_content);
    loadGameContent();
    manual.addClass("disabled");
    new_game.addClass("disabled");
}

// Game Control
function startGame() {
    start_game_btn.addClass("disabled");
    pause_game_btn.removeClass("disabled");
}

function pauseGame() {
    start_game_btn.removeClass("disabled");
    pause_game_btn.addClass("disabled");
}

function stopGame() {
    game.html(home_content);
    manual.removeClass("disabled");
    new_game.removeClass("disabled");
}

// Load game goal and players content
function loadGameContent() {
    getParamValue(score_goal_limit, displayGoalLimit);
    getParamValue(score_name_1, displayPlayerName, "name_player_1");
    getParamValue(score_name_2, displayPlayerName, "name_player_2");
    getParamValue(score_name_3, displayPlayerName, "name_player_3");
    getParamValue(score_name_4, displayPlayerName, "name_player_4");
    getParamValue(score_player_limit, adjustViewedPlayers);
}

function adjustViewedPlayers(nplayer) {
    for(i = 1; i <= MAX_NUMBER_PLAYERS; i++) {
        var id = "#player_" + String(i);
        if(i <= nplayer) {
            $(id).css("visibility", "visible");
        }
        else {
            $(id).css("visibility", "hidden");
        }
    }
}

function displayGoalLimit(value) {
    document.getElementById("goal_limit").innerHTML = value;
}

function displayPlayerName(value, id) {
    document.getElementById(id).innerHTML = value;
}


// Update Score