createJoystick = function () {
    var options = {
        zone: document.getElementById('zone_joystick'),
        threshold: 0.1,
        position: { left: 50 + '%' },
        mode: 'static',
        size: 200,
        color: '#dc3545',
    };
    
    manager = nipplejs.create(options);

    linear_speed = 0;
    angular_speed = 0;

    self.manager.on('start', function (event, nipple) {
      console.log("Movement start");
    });

    self.manager.on('move', function (event, nipple) {
      console.log("Moving");
    });

    self.manager.on('end', function () {
      console.log("Movement end");
    });
  }
  window.onload = function () {
    createJoystick();
  }