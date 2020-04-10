// Game Parameters Constants 
const MAX_NUMBER_GOALS = 15;
const DEFAULT_NUMBER_GOALS = 5;
const MAX_NUMBER_PLAYERS = 4;
const DEFAULT_NUMBER_PLAYERS = 1;

// Establish ROS connection
var ros = new ROSLIB.Ros({
    url : 'ws://localhost:9090'
});

ros.on('connection', function() {
    console.log('Connected to websocket server.');
});

// Parameter server interaction
function createParamObject(name) {
    var param = new ROSLIB.Param({
        ros : ros,
        name : name
      });
    return param;
}

function getScoreParamValue(name) {
    var param = createParamObject("/score/" + name);
    param.get(function(value) {
        return value;
    });
}

function getMotorParamValue(name) {
    var param = createParamObject("/motor_controls_node/"+ name);
    param.get(function(value) {
        return value;
    });
}

// scoreConfig Parameters
var number_goals = getScoreParamValue("goal_limit");
var number_players = getScoreParamValue("player_limit");
var name_1 = getScoreParamValue("name_player_1");
var name_2 = getScoreParamValue("name_player_2");
var name_3 = getScoreParamValue("name_player_3");
var name_4 = getScoreParamValue("name_player_4");

// motorConfig Parameter
var joystick_speed = getMotorParamValue("manual_speed_ratio");