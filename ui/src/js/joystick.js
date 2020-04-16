// Joystick

// Publisher
var joy_publisher = new ROSLIB.Topic({
  ros : ros,
  name : "/joy_pos",
  messageType : 'geometry_msgs/Point'
});

// Function
move = function (posx, posy) {
  var Point = new ROSLIB.Message({
      x: posx,
      y: posy,
      z: 0,
  });
  joy_publisher.publish(Point);
}

// Creating joystick

createJoystick = function () {
  var options = {
    zone: document.getElementById('zone_joystick'),
    threshold: 0.1,
    position: { left: 0 + 'px' },         // necessary in order for the joystick to move
    mode: 'static',
    size: 150,
    color: '#28a745'
  };

  manager = nipplejs.create(options);

  self.manager.on('start', function (event, nipple) {
    timer = setInterval(function () {
      move(joyx, joyy);
    }, 25);
  });

  self.manager.on('move', function (event, nipple) {
    basic_speed = 0.01;
    max_distance = 75.0; // pixels;
    joyx = (Math.sin(nipple.angle.radian) * basic_speed * nipple.distance/max_distance);
    joyy = (-Math.cos(nipple.angle.radian) * basic_speed * nipple.distance/max_distance);
  });

  self.manager.on('end', function () {
    if (timer) {
      clearInterval(timer);
    }
    self.move(0, 0);
  });
  
  return manager;
}

  