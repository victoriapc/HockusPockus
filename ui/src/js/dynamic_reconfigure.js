// Connecting to ROS
// -----------------

var ros = new ROSLIB.Ros({
    url : 'ws://localhost:9090'
});

ros.on('connection', function() {
    console.log('Connected to websocket server.');
});

ros.on('error', function(error) {
    console.log('Error connecting to websocket server: ', error);
});

ros.on('close', function() {
    console.log('Connection to websocket server closed.');
});

// Setting dynamic_reconfigurable parameters using ROS services
// -----------------

var dynaRecClient = new ROSLIB.Service({
    ros : ros,
    name : '/motor_controls_node/set_parameters',
    serviceType : 'dynamic_reconfigure/Reconfigure'
});

function createRequest(val) {
    var request = new ROSLIB.ServiceRequest({
        config: {
            bools: [
                // {name: '', value: false}
            ],
            ints: [
                {name: 'manual_speed_ratio', value: val}
            ],
            strs: [
                // {name: '', value: ''}
            ],
            doubles: [
                // {name: '', value: ''}
            ],
            groups: [
                // {name: '', state: false, id: 0, parent: 0}
            ]
        }
    });
    return request;
}

function updateValue(val) {
    var param = createRequest(val);
    dynaRecClient.callService(request, function(result) {
    console.log('Result for service call on '
        + dynaRecClient.name
        + ': '
        + JSON.stringify(result, null, 2));
    });
}
