// Game Difficulty
const EASY = "Easy";
const MEDIUM = "Medium";
const HARD = "Hard";

// Game parameters
var names;

// Connecting to ROS
var ros = new ROSLIB.Ros({
    url : 'ws://localhost:9090'
});

ros.on('connection', function() {
    console.log('Connected to websocket server.');
});

// ----- Publishers -----
function createPublisher(topicName, msgType) {
    var pub = new ROSLIB.Topic({
        ros : ros,
        name : topicName,
        messageType : msgType
    });
    return pub;
}

function createMsg(val) {
    var msg = new ROSLIB.Message({
        data: val
    })
    return msg;
}

var start_game_pub = createPublisher('/game/start_game', 'std_msgs/Bool');
var strategy_mode_pub = createPublisher('strategy_mode', 'std_msgs/String');

// Create game
function newGame(mode) {
    game.html(game_content);

    loadGameContent();
    document.getElementById("difficulty").innerHTML = mode;

    var strategy_mode_msg = createMsg(mode);
    strategy_mode_pub.publish(strategy_mode_msg);

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
    var start_game_msg = createMsg(true);
    start_game_pub.publish(start_game_msg);

    $("#start_game").addClass("disabled");
    $("#pause_game").removeClass("disabled");
}

function pauseGame() {
    $("#start_game").removeClass("disabled");
    $("#pause_game").addClass("disabled");
}

function stopGame() {
    var start_game_msg = createMsg(false);
    start_game_pub.publish(start_game_msg);

    game.html(home_content);
    manual.removeClass("disabled");
    new_game.removeClass("disabled");
}

// Update Score