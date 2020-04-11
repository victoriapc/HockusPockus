// Establish ROS connection
var ros = new ROSLIB.Ros({
    url : 'ws://localhost:9090'
});

// Motor node dynamic reconfigure client
var motor_client = new ROSLIB.Service({
    ros : ros,
    name : '/motor_controls_node/set_parameters',
    serviceType : 'dynamic_reconfigure/Reconfigure'
});

function createMotorRequest() {
    var request = new ROSLIB.ServiceRequest({
        config: {
            ints: [
                {name: 'manual_speed_ratio', value: Number($("#joystick-speed").val())}
            ]
        }
    });
    return request;
}

function updateMotorConfig() {
    var request = createMotorRequest();
    motor_client.callService(request, function(result) {
        console.log(motor_client.name + " was called.")
    });
}

// Score node dynamic reconfigure client
var score_client = new ROSLIB.Service({
    ros : ros,
    name : '/score/set_parameters',
    serviceType : 'dynamic_reconfigure/Reconfigure'
});

function createScoreRequest() {
    var request = new ROSLIB.ServiceRequest({
        config: {
            ints: [
                {name: 'player_limit', value: Number($("#nplayers").val())},
                {name: 'goal_limit', value: Number($("#ngoals").val())}
            ],
            strs: [
                {name: 'name_player_1', value: $("#name_1").val()},
                {name: 'name_player_2', value: $("#name_2").val()},
                {name: 'name_player_3', value: $("#name_3").val()},
                {name: 'name_player_4', value: $("#name_4").val()}
            ]
        }
    });
    return request;
}

function updateScoreConfig() {
    var request = createScoreRequest();
    score_client.callService(request, function(result) {
        console.log(score_client.name + " was called.")
    });
}
