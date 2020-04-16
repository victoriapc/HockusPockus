// Establish ROS connection
var ros = new ROSLIB.Ros({
    url : 'ws://localhost:9090'
});

// Publisher related functions
function createPublisher(topicName, msgType) {
    var pub = new ROSLIB.Topic({
        ros : ros,
        name : topicName,
        messageType : msgType
    });
    return pub;
}

function createStringMsg(val) {
    var msg = new ROSLIB.Message({
        data: val
    })
    return msg;
}

function createBoolMsg(val) {
    var msg = new ROSLIB.Message({
        data: val
    })
    return msg;
}

function createInt32Msg(val) {
    var msg = new ROSLIB.Message({
        data : Number(val)
    });
    return msg;
}

function createPointMsg(x, y) {
    var msg = new ROSLIB.Message({
        x: x,
        y: y,
        z: 0
    })
    return msg;
}

// Listener related functions
function createSubscriber(topicName, msgType) {
    var sub = new ROSLIB.Topic({
        ros : ros,
        name : topicName,
        messageType : msgType
    });
    return sub;
}
