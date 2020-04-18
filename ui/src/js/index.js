/* ----------------------------------------- */
/* --------------- VARIABLES --------------- */
/* ----------------------------------------- */

// Control Mode
var modeManual = false;
var modeGame = false;

// Joystick Instance
var joystick_manager;

/* ----------------------------------------- */
/* ---------------- ON LOAD ---------------- */
/* ----------------------------------------- */

// DOM Variables
document.addEventListener("DOMContentLoaded", function(){
  updateGameContent(home_content);
});

/* ----------------------------------------- */
/* --------------- New Game ---------------- */
/* ----------------------------------------- */

// See game.js for code

/* ----------------------------------------- */
/* ------------- Manual Control ------------ */
/* ----------------------------------------- */

function manualStart() {
  if(!modeManual) {
    modeManual = true;
    updateGameContent(manual_content);
    $("#new_game").addClass("disabled");
    joystick_manager = createJoystick();
  }
}

function manualStop() {
  if(modeManual) {
    modeManual = false;
    updateGameContent(home_content);
    $("#new_game").removeClass("disabled");
    joystick_manager.destroy();
  }
}

/* ----------------------------------------- */
/* ----------- Information Card ------------ */
/* ----------------------------------------- */

// ROS Status
ros.on('connection', function () {
  document.getElementById("status").innerHTML = "Connected";
});

ros.on('error', function (error) {
  document.getElementById("status").innerHTML = "Error";
});

ros.on('close', function () {
  document.getElementById("status").innerHTML = "Closed";
});

// Video


/* ----------------------------------------- */
/* ------------ Position  Card ------------- */
/* ----------------------------------------- */

// Robot's position listener
var robot_pos_listener = createSubscriber("/robot_pos", "geometry_msgs/Point");

robot_pos_listener.subscribe(function(message) {
  updateRobotPosition(message);
});

function updateRobotPosition(m) {
  document.getElementById("robot_x").innerHTML = m.x.toFixed(3);  // Show only 3 number of precision
  document.getElementById("robot_y").innerHTML = m.y.toFixed(3);
}

// Puck's position listener
var puck_pos_listener = createSubscriber("/puck_pos", "geometry_msgs/Point")

puck_pos_listener.subscribe(function(message) {
  updatePuckPosition(message);
});

function updatePuckPosition(m) {
  document.getElementById("puck_x").innerHTML = m.x.toFixed(3);   // Show only 3 number of precision
  document.getElementById("puck_y").innerHTML = m.y.toFixed(3);
}

/* ----------------------------------------- */
/* -------------- Game Section ------------- */
/* ----------------------------------------- */

const home_content = "<h3>Welcome to the Hockus Pockus User Interface!</h3><p>The UI allows you to control the robot, start a game, configure the webcam's parameters and more. You can navigate through the different pages with the navbar :</p><ul class='nav-content'><li class='nav-content-item'><img src='https://img.icons8.com/ios/100/000000/home.png'><p>-</p><p>Home page to start a game or to control the robot manually</p></li><li class='nav-content-item'><img src='https://img.icons8.com/carbon-copy/100/000000/rules.png'><p>-</p><p>General rules on how to play depending on the number of players</p></li><li class='nav-content-item'><img src='https://img.icons8.com/ios/100/000000/webcam.png'><p>-</p><p>Configure the webcam to optimize the puck finding algorithm</p></li><li class='nav-content-item'><img src='https://img.icons8.com/ios/100/000000/settings.png'><p>-</p><p>Configure the user's and table's parameters</p></li><li class='nav-content-item'><img src='resources/github.png'><p>-</p><p>Access the project source code and the Wiki on Github</p></li></ul>";
const manual_content = "<h3 id='manual-title'>Manual Control</h3><p>The joystick can be used to move the robot. The desired position is published on a ROS topic and the robot moves accordingly.</p><div class='manual-info'><div class='manual-info-title'><p>Desired position</p></div><div class='manual-info-coordinate'><p>X:<span id='manual_x'></span></p><p>Y:<span id='manual_y'></span></p></div></div>";
const game_content = "<h2> First to <span id='goal_limit'></span> wins!</h2><ul id='player-container' class='score'><li class='score-item'><div class='score-item-content'><img id='robot-img' src='https://img.icons8.com/ios/50/000000/bot.png'/></div><img id='equal' src='https://img.icons8.com/ios-filled/50/000000/equal-sign.png'/><div class='score-item-content' id='score-robot'>0</div></li></ul><p class='difficulty-info'>Difficulty: <span id='difficulty'></span></p><div class='game-btn'><button class='btn' id='stop_game' onclick='stopGame()'><img src='https://img.icons8.com/ios-filled/24/000000/stop.png'/></button><button class='btn disabled' id='pause_game' onclick='pauseGame()'><img src='https://img.icons8.com/ios-filled/24/000000/pause.png'/></button><button class='btn' id='start_game' onclick='startGame()'><img src='https://img.icons8.com/ios-filled/24/000000/play.png'/></button></div>";

function updateGameContent(html) {
  $("#game").html(html);
}

// Manual control desired position info
var desired_pos_sub = createSubscriber("/desired_pos", "geometry_msgs/Point")
desired_pos_sub.subscribe(function(message) {
  updateManualDesiredPosition(message);
});

function updateManualDesiredPosition(m) {
  document.getElementById("manual_x").innerHTML = m.x.toFixed(3);
  document.getElementById("manual_y").innerHTML = m.y.toFixed(3);
}