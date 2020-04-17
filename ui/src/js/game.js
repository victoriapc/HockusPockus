// Game Difficulty
const EASY = "Easy";
const MEDIUM = "Medium";
const HARD = "Hard";

// Game parameters
var names;


// Publishers
var start_game_pub = createPublisher('/game/start_game', 'std_msgs/Bool');
var strategy_mode_pub = createPublisher('strategy_mode', 'std_msgs/String');

// Create game
function newGame(mode) {
    updateGameContent(game_content);
    loadGameParameters(mode);
    
    var strategy_mode_msg = createStringMsg(mode);
    strategy_mode_pub.publish(strategy_mode_msg);

    $("#manual").addClass("disabled");
    $("#new_game").addClass("disabled");
}

// Load game goal and players content
function loadGameParameters(mode) {
    getParamValue(score_goal_limit, displayGoalLimit);
    getParamValue(score_names, displayAllPlayers);
    displayDifficulty(mode);
}

function displayDifficulty(mode) {
    document.getElementById("difficulty").innerHTML = mode;
}

function displayGoalLimit(value) {
    document.getElementById("goal_limit").innerHTML = value;
}

function displayAllPlayers(value) {
    names = splitNames(value);

    for(i = 0; i < names.length; i++) {
        addPlayerDiv(i + 1, names[i]);
    }
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
    var start_game_msg = createBoolMsg(true);
    start_game_pub.publish(start_game_msg);

    $("#start_game").addClass("disabled");
    $("#pause_game").removeClass("disabled");
}

function pauseGame() {
    $("#start_game").removeClass("disabled");
    $("#pause_game").addClass("disabled");
}

function stopGame() {
    var start_game_msg = createBoolMsg(false);
    start_game_pub.publish(start_game_msg);

    updateGameContent(home_content);
    $("#manual").removeClass("disabled");
    $("#new_game").removeClass("disabled");
}

// Update Score
var score_subscriber = createSubscriber("scores", "std_msgs/String");
score_subscriber.subscribe(function(message) {
    updateScore(message);
});

function updateScore(message) {
    var dict = createDictionnaryFromString(message);
    for(i = 0; i < names.length; i++) {
        addPlayerDiv(i + 1, names[i]);
    }
}

function createDictionnaryFromString(string) {
    
}

function updateRobotScore(val) {
    
}