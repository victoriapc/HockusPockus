// Game Parameters Constants 
const MAX_NUMBER_GOALS = 15;
const DEFAULT_NUMBER_GOALS = 5;
const MAX_NUMBER_PLAYERS = 4;
const DEFAULT_NUMBER_PLAYERS = 1;

var score_goal_limit = "/score/goal_limit";
var score_player_limit = "/score/player_limit";
var score_name_1 = "/score/name_player_1";
var score_name_2 = "/score/name_player_2";
var score_name_3 = "/score/name_player_3";
var score_name_4 = "/score/name_player_4";

var motor_manual_speed = "/motor_controls_node/manual_speed_ratio";

// Establish ROS connection
var ros = new ROSLIB.Ros({
    url : 'ws://localhost:9090'
});

ros.on('connection', function() {
    console.log('Connected to websocket server.');
});

// Parameter server interaction
function getParamValue(name, callback) {
    var param = createParamObject(name);
    var arg = arguments[2];         // In case an other argument is needed for the callback function
    param.get(function(value) {
        callback(value, arg);
    });
}

function createParamObject(name) {
    var param = new ROSLIB.Param({
        ros : ros,
        name : name
      });
    return param;
}