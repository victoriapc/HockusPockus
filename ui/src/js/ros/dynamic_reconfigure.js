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

function createScoreRequest(names) {
    var request = new ROSLIB.ServiceRequest({
        config: {
            ints: [
                {name: 'goal_limit', value: Number($("#ngoals").val())}
            ],
            strs: [
                {name: 'name_players', value: names},
            ]
        }
    });
    return request;
}

function updateScoreConfig(names) {
    var request = createScoreRequest(names);
    score_client.callService(request, function(result) {
        console.log(score_client.name + " was called.")
    });
}

// Strategy node dynamic reconfigure client
var strategy_client = new ROSLIB.Service({
    ros : ros,
    name : '/strategy/set_parameters',
    serviceType : 'dynamic_reconfigure/Reconfigure'
});

function createStrategyRequest() {
    var request = new ROSLIB.ServiceRequest({
        config: {
            doubles: [
                {name: 'table_height', value: Number($("#height").val())},
                {name: 'table_width', value: Number($("#width").val())}
            ]
        }
    });
    return request;
}

function updateStrategyConfig() {
    var request = createStrategyRequest();
    strategy_client.callService(request, function(result) {
        console.log(strategy_client.name + " was called.")
    });
}
