// Game Parameters Constants 
const MAX_NUMBER_GOALS = 15;
const DEFAULT_NUMBER_GOALS = 5;
const MAX_NUMBER_PLAYERS = 4;
const DEFAULT_NUMBER_PLAYERS = 1;

var score_goal_limit = "/score/goal_limit";
var score_names = "/score/name_players";
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
    param.get(function(value) {
        callback(value);
    });
}

function createParamObject(name) {
    var param = new ROSLIB.Param({
        ros : ros,
        name : name
      });
    return param;
}

function getNames(string) {
    var names = string.split(";");
    return names;
}