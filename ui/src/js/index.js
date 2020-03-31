/* VARIABLES */
// Const
const EASY = 0;
const MEDIUM = 1;
const HARD = 2;

// Section
var new_game = null;
var manual = null;
var game = null;

var modeManual = false;
var modeGame = false;

// Joystick
var joystick_manager;

/* ----- ONLOAD ----- */
// Load ROSLIB library
var ros = new ROSLIB.Ros({
  url: 'ws://localhost:9090'
});

// Load DOM variables
document.addEventListener("DOMContentLoaded", function(){
  loadVar();
  loadContent();
});

function loadVar() {
  new_game = $("#new_game");
  manual = $("#manual");
  game = $("#game");
}

function loadContent() {
  game.html(home_content);
}

/* ----- New game section ----- */
function easy() {
  newGame(EASY);
}

function medium() {
  newGame(MEDIUM);
}

function hard() {
  newGame(HARD);
}

function newGame(mode) {
  game.html(game_content);
  manual.addClass("disabled");
  new_game.addClass("disabled");
}

function stopGame() {
  game.html(home_content);
  manual.removeClass("disabled");
  new_game.removeClass("disabled");
}

/* ----- Manual section ----- */
// Publisher
cmd_vel_publisher = new ROSLIB.Topic({
  ros : ros,
  name : "/cmd_vel",
  messageType : 'geometry_msgs/Twist'
});

move = function (linear, angular) {
  var twist = new ROSLIB.Message({
    linear: {
      x: linear,
      y: 0,
      z: 0
    },
    angular: {
      x: 0,
      y: 0,
      z: angular
    }
  });
  cmd_vel_publisher.publish(twist);
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

/* ----- Information section ----- */
// Conncetion
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


/* ----- Position section ----- */
// Robot's position listener
var robot_pos_listener = new ROSLIB.Topic({
  ros : ros,
  name : '/robot_pos',
  messageType : 'geometry_msgs/Point'
});

function updateRobotPosition(m) {
  document.getElementById("robot_x").innerHTML = 'X: ' + m.x;
  document.getElementById("robot_y").innerHTML = 'Y: ' + m.y;
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
  document.getElementById("puck_x").innerHTML = 'X: ' + m.x;
  document.getElementById("puck_y").innerHTML = 'Y: ' + m.y;
}

puck_pos_listener.subscribe(function(message) {
  updatePuckPosition(message);
});

/* Game Section various content */
const home_content = "<h1>Home</h1>";

const manual_content = "<h1>Manual</h1>"

const game_content = "<h1>Game</h1><button class='btn' onclick='stopGame()' style='background-color: #28a745;'>Stop</button>";

