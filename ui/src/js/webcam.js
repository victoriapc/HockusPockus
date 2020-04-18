// Radius
var radius_slider = null;
var radius_text = null;

// HSV
var h_slider = null;
var h_text = null;
var h_proposed;

var s_slider = null;
var s_text = null;
var s_proposed;

var v_slider = null;
var v_text = null;
var v_proposed;

// Variables
var config_started = false;

var start_pub = createPublisher('/vision/reconfigure/start', 'std_msgs/Bool');
var radius_pub = createPublisher('/vision/reconfigure/radius', 'std_msgs/Int32');
var h_pub = createPublisher('/vision/reconfigure/h', 'std_msgs/Int32');
var s_pub = createPublisher('/vision/reconfigure/s', 'std_msgs/Int32');
var v_pub = createPublisher('/vision/reconfigure/v', 'std_msgs/Int32');
var apply_pub = createPublisher('/vision/reconfigure/apply', 'std_msgs/Bool');
var reset_pub = createPublisher('/vision/reconfigure/resetHSV', 'std_msgs/Bool');

var desired_pos_pub = createPublisher("/desired_pos", "geometry_msgs/Point");

// HSV values subscriber
var h_sub = createSubscriber('/vision/reconfigure/h', 'std_msgs/Int32');
var s_sub = createSubscriber('/vision/reconfigure/s', 'std_msgs/Int32');
var v_sub = createSubscriber('/vision/reconfigure/v', 'std_msgs/Int32');

h_sub.subscribe(function(message) {
    h_proposed = message.data;
    h_slider.value = h_proposed;
    h_text.innerHTML = h_proposed;
});

s_sub.subscribe(function(message) {
    s_proposed = message.data;
    s_slider.value = s_proposed;
    s_text.innerHTML = s_proposed;
});

v_sub.subscribe(function(message) {
    v_proposed = message.data;
    v_slider.value = v_proposed;
    v_text.innerHTML = v_proposed;
});

// Once the DOM is loaded
document.addEventListener("DOMContentLoaded", function(){
    loadSection();
    initSlider();
    loadRatios();
    loadTableDimensions();
    step_1();
});

function loadSection() {
    radius_slider = document.getElementById("r");
    radius_text = document.getElementById("r_text");

    h_slider = document.getElementById("h");
    h_text = document.getElementById("h_text");

    s_slider = document.getElementById("s");
    s_text = document.getElementById("s_text");

    v_slider = document.getElementById("v");
    v_text = document.getElementById("v_text");
}

function initSlider() {
    radius_text.innerHTML = radius_slider.value; 
    h_text.innerHTML = h_slider.value;
    s_text.innerHTML = s_slider.value;
    v_text.innerHTML = v_slider.value;
}

// When window is closing
window.onbeforeunload = function(){
    if(config_started) {
        return "Are you sure?";
    }
};

// Hidding section for the sequence
function step_1() {
    $("#start").removeClass("disabled");
    $("#corners").addClass("disabled");
    $("#radius").addClass("disabled");
    $("#hsv").addClass("disabled");
};

function step_2() {
    var start_msg = createBoolMsg(true);
    start_pub.publish(start_msg);

    var pos_msg = createPointMsg(0, 0);
    desired_pos_pub.publish(pos_msg);

    $("#corners-apply").prop("disabled", true);
    startListeningToClicks();

    config_started = true;
    $("#start").addClass("disabled");
    $("#corners").removeClass("disabled");

    alert("Adjust the dimensions of the table while the robot moves to the (0, 0) position. Once it stops to move, click on its position.")
}

function step_3() {
    updateStrategyConfig();

    $("#corners").addClass("disabled");
    $("#radius").removeClass("disabled");
}

function step_4() {
    var apply_msg = createBoolMsg(true);
    apply_pub.publish(apply_msg);

    $("#radius").addClass("disabled");
    $("#hsv").removeClass("disabled");
    config_started = false;
}

function resetHSV() {
    var reset_msg = createBoolMsg(true);
    reset_pub.publish(reset_msg);
}

function apply() {
    var apply_msg = createBoolMsg(true);
    apply_pub.publish(apply_msg);

    step_1();
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


// Calculate video ratio
var heigth_ratio;
var width_ratio;

function setWidthRatio(value) {
    width_ratio = value/getVideoWidth();
}

function setHeightRatio(value) {
    height_ratio = value/getVideoHeight();
}

function getVideoHeight() {
    return $("#video").height();
}

function getVideoWidth() {
    return $("#video").width();
}

function loadRatios() {
    getParamValue(webcam_height, setHeightRatio);
    getParamValue(webcam_width, setWidthRatio);
}

// Table dimensions interaction
var table_height;
var table_width;

function displayTableWidth(value) {
    $("#width").prop("value", value);
}

function displayTableHeight(value) {
    $("#height").prop("value", value);
}

function loadTableDimensions() {
    getParamValue(strategy_table_height, displayTableHeight);
    getParamValue(strategy_table_width, displayTableWidth);
}

// Mouse event interaction
var nclicks = 0;
var point_pub = createPublisher("/ui/mouse_event", "geometry_msgs/Point");

function startListeningToClicks() {
    $("#video").on('click', function(event) {
        manageCoordinate(event, this);
    });
}

function stopListeningToClicks() {
    $("#video").off('click');
}

function manageCoordinate(event, obj) {
    var x = (event.pageX - obj.offsetLeft)*width_ratio;
    var y = (event.pageY - obj.offsetTop)*height_ratio;
    
    publishCoordinate(x, y);
    nclicks++;

    if(nclicks == 1) {
        var pos_msg = createPointMsg(Number($("#width").val()), Number($("#height").val()));
        desired_pos_pub.publish(pos_msg);

        alert("Wait for the robot to stop moving. Click on its position once again.");
    }

    if(nclicks == 2) {
        stopListeningToClicks();
        $("#corners-apply").prop("disabled", false);
        var pos_msg = createPointMsg(0, 0);
        desired_pos_pub.publish(pos_msg);
    }
}

function publishCoordinate(x, y) {
    var point_msg = createPointMsg(x, y);
    point_pub.publish(point_msg);
}