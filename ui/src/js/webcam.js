// Radius
var radius_slider = null;
var radius_text = null;

// HSV
var h_slider = null;
var h_text = null;
var s_slider = null;
var s_text = null;
var v_slider = null;
var v_text = null;

// Variables
var config_started = false;

var start_pub = createPublisher('/vision/reconfigure/start', 'std_msgs/Bool');
var radius_pub = createPublisher('/vision/reconfigure/radius', 'std_msgs/Int32');
var h_pub = createPublisher('/vision/reconfigure/h', 'std_msgs/Int32');
var s_pub = createPublisher('/vision/reconfigure/s', 'std_msgs/Int32');
var v_pub = createPublisher('/vision/reconfigure/v', 'std_msgs/Int32');
var apply_pub = createPublisher('/vision/reconfigure/apply', 'std_msgs/Bool');

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
    //var apply_msg = createBoolMsg(true);
    //apply_pub.publish(apply_msg);

    $("#start").removeClass("disabled");
    $("#corners").addClass("disabled");
    $("#radius").addClass("disabled");
    $("#hsv").addClass("disabled");
};

function step_2() {
    var start_msg = createBoolMsg(true);
    start_pub.publish(start_msg);

    startListeningToClicks();

    config_started = true;
    $("#start").addClass("disabled");
    $("#corners").removeClass("disabled");

    alert("Click on the bottom left corner.")
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

    console.log(y);
    
    publishCoordinate(x, nclicks*50);
    nclicks++;

    if(nclicks == 1) {
        alert("Click on the top-rigth corner.");
    }

    if(nclicks == 2) {
        stopListeningToClicks();
        alert("Corners position sent. You can adjust the size the table dimensions.")
    }
}

function publishCoordinate(x, y) {
    var point_msg = createPointMsg(x, y);
    point_pub.publish(point_msg);
}