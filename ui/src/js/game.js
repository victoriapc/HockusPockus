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
    adjustViewedPlayers(number_players);
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
    document.getElementById("goal_limit").innerHTML = number_goals;
    document.getElementById("name_player_1").innerHTML = name_1;
    document.getElementById("name_player_2").innerHTML = name_2;
    document.getElementById("name_player_3").innerHTML = name_3;
    document.getElementById("name_player_4").innerHTML = name_4;
}

function adjustViewedPlayers(nplayer) {
    for(i = nplayer; i <= MAX_NUMBER_PLAYERS; i++) {
        var id = "#player_" + String(i);
        if(i <= nplayer) {
            $(id).css("visibility", "visible");
        }
        else {
            $(id).css("visibility", "hidden");
        }
    }
}


// Update Score