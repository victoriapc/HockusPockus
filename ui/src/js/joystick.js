// Joystick

// Publisher
var joy_publisher = createPublisher("/joy_pos", "geometry_msgs/Point");

move = function (posx, posy) {
  var Point = createPointMsg(posx, posy);
  joy_publisher.publish(Point);
}

//main joystick function
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

  