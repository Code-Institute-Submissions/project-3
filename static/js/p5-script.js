let canvas;
let dot;
let backImg;
let originalX = 215;
let originalY = 132;
let currentX, currentY;
let hoverX, hoverY;

function preload() {
  backImg = loadImage('../static/img/myLogoimage_clean_id.png');
  dot = loadImage('../static/img/small_section_logo.png');
}

function setup() {
  canvas = createCanvas(276, 200);
  // cnv.position(50, 50);
  canvas.parent('sketchHolder');
  // canvas.parent.style('position', 'absolute');
  // canvas.parent.style('top', '32px');
  // canvas.parent.style('left', '35px');
  currentX = originalX;
  currentY = originalY;
  image(dot, currentX, currentY);
  // image(dot, originalX, originalY, dot.width, dot.height);
}

function draw() {
  background(0,0);
  imageMode(CORNER);
  image(backImg, 0, 0, 276, 200);
  // texture(backImg);
  // rect(0, 0, 276, 200);
  // fill(255, 0, 0, 0);
  // noStroke();
  // stroke(0);
  // strokeWeight(1);
  // rect(203, 120, 21, 24);
  // image(dot, 203, 120, dot.width, dot.height);


  hoverX = mouseX;
  hoverY = mouseY;
  imageMode(CENTER);
  if (hoverX > 0 && hoverX < 276 && hoverY > 0 && hoverY < 200) {
    currentX = (currentX + hoverX)/3;
    currentY = (currentY + hoverY)/3;
    scale(2);
    image(dot, currentX, currentY);
  } else {
    currentX = (currentX + originalX)/2;
    currentY = (currentY + originalY)/2;
    image(dot, currentX, currentY);
  }
  
}


// function setup() {
//   var canvas = createCanvas(100, 100);
 
//   // Move the canvas so it’s inside our <div id="sketch-holder">.
//   canvas.parent('sketch-holder');

//   background(255, 0, 200);
// }