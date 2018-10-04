let canvas;
// let dot;
// let backImg;
let backImgFull, backImgWords, imgExclamation;

let originalX = 215;
let originalY = 132;
let currentX, currentY;
let hoverX, hoverY;
let imgMarginLeft;
let logoImage;
let sketchHolder;

let windowWidth;



function preload() {
  // backImg = loadImage('../static/img/myLogoimage_clean_id.png');
  // dot = loadImage('../static/img/small_section_logo.png');
  backImgFull = loadImage('../static/img/guess_full_wood_700x569.min1.png');
  backImgWords = loadImage('../static/img/guess_words_only_700x569.min1.png');
  imgExclamation = loadImage('../static/img/guess_exclamation_mark_wood_102x318.min3.png');
}

function setup() {
  logoImage = document.getElementById("logoImage");
  imgMarginLeft = logoImage.offsetLeft;
  // console.log(imgMarginLeft);
  canvas = createCanvas(276, 200);
  // cnv.position(50, 50);
  canvas.parent('sketchHolder');
  // canvas.parent.style('position', 'absolute');
  // canvas.parent.style('top', '32px');
  // canvas.parent.style('left', '35px');

  sketchHolder = document.getElementById("sketchHolder");
  sketchHolder.style.left = imgMarginLeft;


  currentX = originalX;
  currentY = originalY;
  // image(imgExclamation, currentX, currentY);

  // image(dot, currentX, currentY);
  // image(dot, originalX, originalY, dot.width, dot.height);
}

function draw() {

  windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

  if (windowWidth > 992) {



    imgMarginLeft = logoImage.offsetLeft;
    // console.log(imgMarginLeft);
    // document.getElementById("#sketchHolder").style.left = imgMarginLeft;
    sketchHolder.style.left = (imgMarginLeft + 15) + "px";
    background(0,0);
    // imageMode(CORNER);
    // image(backImg, 0, 0, 276, 200);
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
    // imageMode(CENTER);
    if (hoverX > 0 && hoverX < 276 && hoverY > 0 && hoverY < 200) {
      currentX = (currentX + hoverX)/2;
      currentY = (currentY + hoverY)/2;
      // scale(2);
      // image(dot, currentX, currentY);
      imageMode(CORNER);
      image(backImgWords, 0, 0, 276, 200);
      imageMode(CENTER);
      image(imgExclamation, currentX-5, currentY - 50, 40, 112 );
    } else {
      currentX = (currentX + originalX)/2;
      currentY = (currentY + originalY)/2;
      // image(dot, currentX, currentY);
      imageMode(CORNER);
      image(backImgFull, 0, 0, 276, 200);
      imageMode(CENTER);
      image(imgExclamation, currentX-5, currentY - 45, 40, 112);
    }
  }
  
}


// function setup() {
//   var canvas = createCanvas(100, 100);
 
//   // Move the canvas so it’s inside our <div id="sketch-holder">.
//   canvas.parent('sketch-holder');

//   background(255, 0, 200);
// }