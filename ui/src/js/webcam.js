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

// Varaibles
var config_started = false;

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
        console.log("Conditon true.")
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
    config_started = true;
    start.addClass("disabled");
    radius.removeClass("disabled");
}

function step_3() {
    radius.addClass("disabled");
    hsv.removeClass("disabled");
}

function step_4() {
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
}

function updateH() {
    h_text.innerHTML = h_slider.value;
}
function updateS() {
    s_text.innerHTML = s_slider.value;
}
function updateV() {
    v_text.innerHTML = v_slider.value;
}