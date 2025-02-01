document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.navbar-burger').addEventListener('click', function () {
        document.querySelector('.navbar-menu').classList.toggle('is-active');
    }
    );
    
});

document.querySelector('#contratar').addEventListener('click', function () {
    
    var duration = 5 * 1000;
var animationEnd = Date.now() + duration;
var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

function randomInRange(min, max) {
  return Math.random() * (max - min) + min;
}

var interval = setInterval(function() {
  var timeLeft = animationEnd - Date.now();

  if (timeLeft <= 0) {
    return clearInterval(interval);
  }

  var particleCount = 50 * (timeLeft / duration);

  // set zindex as 55
    defaults.zIndex = 55;
  // since particles fall down, start a bit higher than random
  confetti({ ...defaults, particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } });
  confetti({ ...defaults, particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } });
}, 250);

document.querySelector('#lets-dance').classList.remove('is-hidden');
setInterval(function () {
    document.querySelector('#dancer').classList.toggle('is-flipped');
}, 2000);

document.querySelector('#happy').play();

});

// when click on stop
document.querySelector('#stop').addEventListener('click', function () {
    document.querySelector('#lets-dance').classList.add('is-hidden');
    //conffeti stop
    clearInterval(interval);   
});