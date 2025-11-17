import gab.opencv.*;
import processing.video.*;
import java.awt.Rectangle;

Capture cam;
OpenCV opencv;

void setup() {
  size(640, 480);
  
  // Inicializar cámara
  cam = new Capture(this, 640, 480);
  cam.start();
  
  // Inicializar OpenCV con el tamaño de la cámara
  opencv = new OpenCV(this, 640, 480);
  
  // Cargar el clasificador HaarCascade para caras
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE);  
}

void draw() {
  if (cam.available()) {
    cam.read();
  }
  
  // Mostrar video
  image(cam, 0, 0);
  
  // Pasar el frame actual a OpenCV
  opencv.loadImage(cam);
  
  // Detectar rostros
  Rectangle[] faces = opencv.detect();
  
  // Dibujar rectángulos sobre cada cara
  noFill();
  stroke(255, 0, 0);
  strokeWeight(3);
  for (int i = 0; i < faces.length; i++) {
    rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height);
  }
}
