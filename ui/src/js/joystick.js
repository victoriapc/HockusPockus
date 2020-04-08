// Joystick
createJoystick = function () {
  var options = {
    zone: document.getElementById('zone_joystick'),
    threshold: 0.1,
    position: { left: 0 + 'px' },         // necessary in order for the joystick to move
    mode: 'static',
    size: 200,
    color: '#28a745'
  };

  manager = nipplejs.create(options);

  self.manager.on('start', function (event, nipple) {
    timer = setInterval(function () {
      move(joyx, joyy,max_speed);
    }, 25);
  });

  self.manager.on('move', function (event, nipple) {
    max_distance = 75.0; // pixels;
    joyx = (Math.sin(nipple.angle.radian) * max_speed * nipple.distance/max_distance);
    joyy = (-Math.cos(nipple.angle.radian) * max_speed * nipple.distance/max_distance);
  });

  self.manager.on('end', function () {
    if (timer) {
      clearInterval(timer);
    }
    self.move(0, 0);
  });
  return manager;
}

  