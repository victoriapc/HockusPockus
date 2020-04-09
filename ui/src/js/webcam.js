// Start
var start = null;

// Radius
var radius = null;
var radius_slider = null;
var radius_text = null;

// HSV
var hsv = null;
var h_slider = null;
var h_text = null;
var s_slider = null;
var s_text = null;
var v_slider = null;
var v_text = null;

// Apply
var apply = null;

// Variables
var config_started = false;

// Connecting to ROS

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

// ----- Publishers -----
function createPublisher(topicName, msgType) {
    var pub = new ROSLIB.Topic({
        ros : ros,
        name : topicName,
        messageType : msgType
    });
    return pub;
}

var start_pub = createPublisher('/vision/reconfigure/start', 'std_msgs/Bool');
var radius_pub = createPublisher('/vision/reconfigure/radius', 'std_msgs/Int32');
var h_pub = createPublisher('/vision/reconfigure/h', 'std_msgs/Int32');
var s_pub = createPublisher('/vision/reconfigure/s', 'std_msgs/Int32');
var v_pub = createPublisher('/vision/reconfigure/v', 'std_msgs/Int32');
var apply_pub = createPublisher('/vision/reconfigure/apply', 'std_msgs/Bool');

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
    console.log(msg);
    return msg;
}

// Once the DOM is loaded
document.addEventListener("DOMContentLoaded", function(){
    loadSection();
    loadSlider();
    step_1();
});

function loadSection() {
    start = $("#start");
    radius = $("#radius");
    radius_slider = document.getElementById("r");
    radius_text = document.getElementById("r_text");
    hsv = $("#hsv");
    h_slider = document.getElementById("h");
    h_text = document.getElementById("h_text");
    s_slider = document.getElementById("s");
    s_text = document.getElementById("s_text");
    v_slider = document.getElementById("v");
    v_text = document.getElementById("v_text");
    apply = $("#apply");
}

// When window is closing
window.onbeforeunload = function(){
    if(config_started) {
        return "Are you sure?";
    }
};

// Hidding section for the sequence
function step_1() {
    start.removeClass("disabled");
    radius.addClass("disabled");
    hsv.addClass("disabled");
    apply.addClass("disabled");
};

function step_2() {
    var start_msg = createBoolMsg(true);
    start_pub.publish(start_msg);

    config_started = true;
    start.addClass("disabled");
    radius.removeClass("disabled");
}

function step_3() {
    radius.addClass("disabled");
    hsv.removeClass("disabled");
}

function step_4() {
    var apply_msg = createBoolMsg(true);
    apply_pub.publish(apply_msg);

    hsv.addClass("disabled");
    apply.removeClass("disabled");
    config_started = false;
}

// Slider linked
function loadSlider() {
    radius_text.innerHTML = radius_slider.value; 
    h_text.innerHTML = h_slider.value;
    s_text.innerHTML = s_slider.value;
    v_text.innerHTML = v_slider.value;
}

// Update the current slider value (each time you drag the slider handle)
function updateR() {
    radius_text.innerHTML = radius_slider.value;
    var radius_msg = createInt32Msg(radius_slider.value);
    radius_pub.publish(radius_msg);
}

function updateH() {
    h_text.innerHTML = h_slider.value;
    var h_msg = createInt32Msg(h_slider.value);
    h_pub.publish(h_msg);
}
function updateS() {
    s_text.innerHTML = s_slider.value;
    var s_msg = createInt32Msg(s_slider.value);
    s_pub.publish(s_msg);
}
function updateV() {
    v_text.innerHTML = v_slider.value;
    var v_msg = createInt32Msg(v_slider.value);
    v_pub.publish(v_msg);
}