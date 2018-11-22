let canvas;
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
  backImgFull = loadImage('../static/img/guess_full_wood_700x569.min1.png');
  backImgWords = loadImage('../static/img/guess_words_only_700x569.min1.png');
  imgExclamation = loadImage('../static/img/guess_exclamation_mark_wood_102x318.min3.png');
}

function setup() {
  logoImage = document.getElementById("logoImage");
  imgMarginLeft = logoImage.offsetLeft;
  canvas = createCanvas(276, 200);
  canvas.parent('sketchHolder');

  sketchHolder = document.getElementById("sketchHolder");
  sketchHolder.style.left = imgMarginLeft;

  currentX = originalX;
  currentY = originalY;
}

function controlImage(thisImage, offset, X, Y) {
  currentX = (currentX + X) / 2;
  currentY = (currentY + Y) / 2;
  imageMode(CORNER);
  image(thisImage, 0, 0, 276, 200);
  imageMode(CENTER);
  image(imgExclamation, currentX - 5, currentY - offset, 40, 112);
}


function draw() {
  // Need to get window width for various browsers
  windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

  if (windowWidth > 992) {
    imgMarginLeft = logoImage.offsetLeft;
    sketchHolder.style.left = (imgMarginLeft + 15) + "px";
    background(0, 0);
    hoverX = mouseX;
    hoverY = mouseY;

    if (hoverX > 0 && hoverX < 276 && hoverY > 0 && hoverY < 200) {
      controlImage(backImgWords, 50, hoverX, hoverY);
    } else {
      controlImage(backImgFull, 45, originalX, originalY);
    }
  }
}