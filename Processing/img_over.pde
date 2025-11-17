import gab.opencv.*;
import processing.video.*;
import java.awt.Rectangle;

Capture cam;
OpenCV opencv;
PImage gorro;

void setup() {
  size(640, 480);
  
  // Inicializar cámara
  cam = new Capture(this, 640, 480);
  cam.start();
  
  // Inicializar OpenCV
  opencv = new OpenCV(this, 640, 480);
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE);
  
  // Cargar imagen que se va a sobreponer (ej. un gorro)
  gorro = loadImage("gorro.png"); // debe estar en la carpeta "data"
}

void draw() {
  if (cam.available()) {
    cam.read();
  }
  
  // Mostrar cámara
  image(cam, 0, 0);
  
  // Detectar rostros
  opencv.loadImage(cam);
  Rectangle[] faces = opencv.detect();
  
  for (int i = 0; i < faces.length; i++) {
    Rectangle f = faces[i];
    
    // Dibujar cuadro de referencia (opcional)
    noFill();
    stroke(0, 255, 0);
    strokeWeight(2);
    rect(f.x, f.y, f.width, f.height);
    
    // Colocar la imagen sobre el rostro
    image(gorro, f.x, f.y, f.width, f.height); 
    // Ajusta la posición y tamaño según la imagen
  }
}
