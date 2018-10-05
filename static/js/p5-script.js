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

function draw() {

  windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

  if (windowWidth > 992) {
    imgMarginLeft = logoImage.offsetLeft;
    sketchHolder.style.left = (imgMarginLeft + 15) + "px";
    background(0, 0);

    hoverX = mouseX;
    hoverY = mouseY;

    if (hoverX > 0 && hoverX < 276 && hoverY > 0 && hoverY < 200) {
      currentX = (currentX + hoverX) / 2;
      currentY = (currentY + hoverY) / 2;
      imageMode(CORNER);
      image(backImgWords, 0, 0, 276, 200);
      imageMode(CENTER);
      image(imgExclamation, currentX - 5, currentY - 50, 40, 112);
    } else {
      currentX = (currentX + originalX) / 2;
      currentY = (currentY + originalY) / 2;
      imageMode(CORNER);
      image(backImgFull, 0, 0, 276, 200);
      imageMode(CENTER);
      image(imgExclamation, currentX - 5, currentY - 45, 40, 112);
    }
  }
}