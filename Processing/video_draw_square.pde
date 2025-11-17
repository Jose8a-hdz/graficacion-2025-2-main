import processing.video.*;

Capture cam;

void setup() { 
  size(640, 480);
  
  // Ver cámaras disponibles
  println(Capture.list());

  // Usar la primera cámara
  cam = new Capture(this, 640, 480);
  cam.start();
}

void draw() {
  if (cam.available()) {
    cam.read();
  }

  // Mostrar el video en pantalla
  image(cam, 0, 0, width, height);

  // Dibujar un cuadro rojo encima
  noFill();
  stroke(255, 0, 0);
  strokeWeight(3);
  rect(200, 150, 200, 150);  // x, y, ancho, alto
}
