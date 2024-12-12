/* IDEAS:
other:  
  potentially feed cat treat; animate a mouth and play crunch sound */

/* creates paragraph element in .cat div; */
var div = document.querySelector('.cat');
var p = document.createElement('p');
div.appendChild(p);
    p.innerHTML = 'Touch me..!'; 
    p.style.color="black";
    p.style.fontSize="50px";
    p.style.fontFamily="impact";
/* global variable to use for animation event listener; finds .head div, which is parent to all other divs; 
NOTE TO SELF: event listeners affect elements and their children regardless of what variable CAT holds; */
var cat = document.querySelector('.head');

/* when mouse clicks any part of cat, it starts pet animation function - tail wag & eyes semi-closed along with purr sound; since there are two different ways to interact with the cat (mouse & touch), there are different event listeners for each to start/stop animations; */
cat.addEventListener('touchmove', petAnimation);
cat.addEventListener('mousemove', petAnimation);

/* function that starts eye movement, tail wag, and purr sound when the cat is "pet"; function that stops the pet animation within it; */
function petAnimation() {
  /* changes .cat paragraph text */
    p.innerHTML = "Welcome to MOVIE MANIA..!"; 
    p.style.color="black";
    p.style.fontSize="50px";
    p.style.fontFamily="impact";
  /* finds all animated body parts for the pet animation - tail and eyes; */
  var animated_parts = document.querySelectorAll('.tail, .left_eyelid, .right_eyelid');
  
  /* loops through length of variable in order to style each element for the animation; play state for .tail is toggled from its default 'paused' state to 'running'; the iteration count for both eyelid classes is changed from its default of '1' to 'infinite'; */
  for (i = 0; i < animated_parts.length; i++) {
    animated_parts[i].style.animationPlayState = 'running';
    animated_parts[i].style.animationIterationCount = 'infinite';
  }
  
  /* plays purr audio when pet; need .mp3 file;
  sound location: https://freesound.org/s/194926/; */
//   var purr_audio = new Audio('https://freesound.org/data/previews/194/194926_1160789-lq.mp3');
//   purr_audio.loop = true;
//   purr_audio.play();
  
  /* two different event listeners for mouse & touch; stops animation when mouse is no longer within cat element or cat is no longer being touched; 
  !!! would like to delay the end of the animation; */
  cat.addEventListener('mouseleave', stopAnimation);
  cat.addEventListener('touchend', stopAnimation);
  
  function stopAnimation() {
    
    p.innerHTML = "Touch me again...!"; 
    
    /* resets .tail animation play state to default play state; reset eyelid iteration count back to default */
    for (i = 0; i < animated_parts.length; i++) {
      animated_parts[i].style.animationPlayState = 'paused';
      animated_parts[i].style.animationIterationCount = '1';
    }
    
    /* pauses cat purr when mouse/touch is removed */
    // purr_audio.pause();
  }
}