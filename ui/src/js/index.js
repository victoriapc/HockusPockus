/* ----------------------------------------- */
/* --------------- VARIABLES --------------- */
/* ----------------------------------------- */

// Game Difficulty
const EASY = 0;
const MEDIUM = 1;
const HARD = 2;

// Game buttons
var start_game_btn = null;
var pause_game_btn = null;
var stop_game_btn = null;

// Sections
var new_game = null;
var manual = null;
var game = null;

// Control Mode
var modeManual = false;
var modeGame = false;

// Joystick Instance
var joystick_manager;

/* ----------------------------------------- */
/* ---------------- ON LOAD ---------------- */
/* ----------------------------------------- */

// ROSLIB library
var ros = new ROSLIB.Ros({
  url: 'ws://localhost:9090'
});

// DOM Variables
document.addEventListener("DOMContentLoaded", function(){
  loadVar();
  game.html(home_content);
});

function loadVar() {
  new_game = $("#new_game");
  manual = $("#manual");
  game = $("#game");

  difficulty_info = $("#difficulty");

  start_game_btn = $("#start_game");
  pause_game_btn = $("#pause_game");
  stop_game_btn = $("#stop_game");
}

/* ----------------------------------------- */
/* --------------- New Game ---------------- */
/* ----------------------------------------- */

// See game.js for code

/* ----------------------------------------- */
/* ------------- Manual Control ------------ */
/* ----------------------------------------- */

// Publisher
var joy_publisher = new ROSLIB.Topic({
  ros : ros,
  name : "/joy_pos",
  messageType : 'geometry_msgs/Point'
});

move = function (posx, posy) {
  var Point = new ROSLIB.Message({
      x: posx,
      y: posy,
      z: 0,
  });
  joy_publisher.publish(Point);
}

function manualStart() {
  if(!modeManual) {
    modeManual = true;
    game.html(manual_content);
    new_game.addClass("disabled");
    joystick_manager = createJoystick();
  }
}

function manualStop() {
  if(modeManual) {
    modeManual = false;
    game.html(home_content);
    new_game.removeClass("disabled");
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
var robot_pos_listener = new ROSLIB.Topic({
  ros : ros,
  name : '/robot_pos',
  messageType : 'geometry_msgs/Point'
});

function updateRobotPosition(m) {
  document.getElementById("robot_x").innerHTML = m.x;
  document.getElementById("robot_y").innerHTML = m.y;
}

robot_pos_listener.subscribe(function(message) {
  updateRobotPosition(message);
});

// Puck's position listener
var puck_pos_listener = new ROSLIB.Topic({
  ros : ros,
  name : '/puck_pos',
  messageType : 'geometry_msgs/Point'
});

function updatePuckPosition(m) {
  document.getElementById("puck_x").innerHTML = m.x;
  document.getElementById("puck_y").innerHTML = m.y;
}

puck_pos_listener.subscribe(function(message) {
  updatePuckPosition(message);
});

/* ----------------------------------------- */
/* -------------- Game Section ------------- */
/* ----------------------------------------- */

const home_content = "<h3>Welcome to the Hockus Pockus User Interface!</h3><p>The UI allows you to control the robot, start a game, configure the webcam's parameters and more. You can navigate through the different pages with the navbar :</p><ul class='nav-content'><li class='nav-content-item'><img src='https://img.icons8.com/ios/100/000000/home.png'><p>-</p><p>Home page to start a game or to control the robot manually</p></li><li class='nav-content-item'><img src='https://img.icons8.com/carbon-copy/100/000000/rules.png'><p>-</p><p>General rules on how to play depending on the number of players</p></li><li class='nav-content-item'><img src='https://img.icons8.com/ios/100/000000/webcam.png'><p>-</p><p>Configure the webcam to optimize the puck finding algorithm</p></li><li class='nav-content-item'><img src='https://img.icons8.com/ios/100/000000/settings.png'><p>-</p><p>Configure the user's and table's parameters</p></li><li class='nav-content-item'><img src='resources/github.png'><p>-</p><p>Access the project source code and the Wiki on Github</p></li></ul>";
const manual_content = "<h3 id='manual-title'>Manual Control</h3><p>The joystick can be used to move the robot. The desired position is published on a ROS topic and the robot moves accordingly.</p><div class='manual-info'><div class='manual-info-title'><p>Desired position</p></div><div class='manual-info-coordinate'><p>X:<span id='manual_x'></span></p><p>Y:<span id='manual_y'></span></p></div></div>";
const game_content = "<h2> First to <span id='goal_limit'></span> wins!</h2><ul class='score'><li class='score-item'><div class='score-item-content'><img id='robot-img' src='https://img.icons8.com/ios/50/000000/bot.png'/></div><img id='equal' src='https://img.icons8.com/ios-filled/50/000000/equal-sign.png'/><span class='score-item-content' id='score-robot'>0</span></li><li id='player_1' class='score-item'><div id='name_player_1' class='score-item-content'></div><img id='equal' src='https://img.icons8.com/ios-filled/50/000000/equal-sign.png'/><div class='score-item-content' id='score-player-1'>0</div></li><li id='player_2' class='score-item'><span id='name_player_2' class='score-item-content'></span><img id='equal' src='https://img.icons8.com/ios-filled/50/000000/equal-sign.png'/><span class='score-item-content' id='score-player-2'>0</span></li><li id='player_3' class='score-item'><span id='name_player_3' class='score-item-content'></span><img id='equal' src='https://img.icons8.com/ios-filled/50/000000/equal-sign.png'/><span class='score-item-content' id='score-player-3'>0</span></li><li id='player_4' class='score-item'><span id='name_player_4' class='score-item-content'></span><img id='equal' src='https://img.icons8.com/ios-filled/50/000000/equal-sign.png'/><span class='score-item-content' id='score-player-4'>0</span></li></ul><p class='difficulty-info'>Difficulty: <span id='difficulty'></span></p><div class='game-btn'><button class='btn' id='stop_game' onclick='stopGame()'><img src='https://img.icons8.com/ios-filled/24/000000/stop.png'/></button><button class='btn disabled' id='pause_game' onclick='pauseGame()'><img src='https://img.icons8.com/ios-filled/24/000000/pause.png'/></button><button class='btn' id='start_game' onclick='startGame()'><img src='https://img.icons8.com/ios-filled/24/000000/play.png'/></button></div>";

// Desired Joystick Position
function updateManualPosition(m) {
  document.getElementById("manual_x").innerHTML = m.x;
  document.getElementById("manual_y").innerHTML = m.y;
}

