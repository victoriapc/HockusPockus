var ros = new ROSLIB.Ros({
  url: 'ws://localhost:9090'
});

ros.on('connection', function () {
  document.getElementById("status").innerHTML = "Connected";
});

ros.on('error', function (error) {
  document.getElementById("status").innerHTML = "Error";
});

ros.on('close', function () {
  document.getElementById("status").innerHTML = "Closed";
});

var txt_listener = new ROSLIB.Topic({
  ros: ros,
  name: '/txt_msg',
  messageType: 'std_msgs/String'
});

txt_listener.subscribe(function (m) {
  document.getElementById("msg").innerHTML = m.data;
});
/* 
var video = document.querySelector("#videoElement");

if (navigator.mediaDevices.getUserMedia) {
navigator.mediaDevices.getUserMedia({ video: true })
  .then(function (stream) {
  video.srcObject = stream;
  })
  .catch(function (err0r) {
  console.log("Something went wrong with video!");
  });
}
*/
var pos_listener = new ROSLIB.Topic({
  ros : ros,
  name : '/puck_pos',
  messageType : 'geometry_msgs/Point'
});

pos_listener.subscribe(function(m) {
  console.log('Received message on ' + pos_listener.name + ': ' + m.x)
  document.getElementById("puck_pos").innerHTML = 'X: ' + m.x + '\nY: ' + m.y;
});