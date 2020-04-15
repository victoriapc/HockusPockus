// Parameters Constants 
var score_goal_limit = "/score/goal_limit";
var score_names = "/score/name_players";
var motor_manual_speed = "/motor_controls_node/manual_speed_ratio";

var webcam_framerate = "/usb_cam/framerate";
var webcam_height = "/usb_cam/image_height";
var webcam_width = "/usb_cam/image_width";

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

// Names manipulation function
function splitNames(string) {
    var names = string.split(";");
    return names;
}

function concatenateNames(names) {
    var string = "";

    for(i = 0; i < (names.length - 1); i++) {
        string += (names[i] + ";");
    }
    string += names[names.length - 1];

    return string;
}