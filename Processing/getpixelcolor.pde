import processing.video.*;

Capture cam;

void setup() {
  size(640, 480);
  
  // Listar cámaras disponibles (opcional)
  String[] cameras = Capture.list();
  println("Cámaras disponibles:");
  for (int i = 0; i < cameras.length; i++) {
    println(i + ": " + cameras[i]);
  }
  
  // Inicializar cámara
  cam = new Capture(this, 640, 480);
  cam.start();
}

void draw() {
  if (cam.available()) {
    cam.read();
  }
  
  // Mostrar video de la cámara
  image(cam, 0, 0);
  
  // Leer el píxel en coordenada (100, 100)
  int x = 100;
  int y = 100;
  
  color c = cam.get(x, y);
  
  // Extraer componentes RGB
  float r = red(c);
  float g = green(c);
  float b = blue(c);
  
  // Imprimir en consola
  println("Píxel en (" + x + ", " + y + "):");
  println("  R: " + r);
  println("  G: " + g);
  println("  B: " + b);
  println("  Hex: #" + hex(c, 6));
  println("---");
  
  // Visualizar la coordenada
  // Dibujar cruz en (100, 100)
  stroke(255, 255, 0);
  strokeWeight(2);
  line(x - 10, y, x + 10, y);
  line(x, y - 10, x, y + 10);
  
  // Dibujar círculo alrededor
  noFill();
  stroke(0, 255, 0);
  strokeWeight(3);
  ellipse(x, y, 20, 20);
  
  // Mostrar muestra del color
  fill(c);
  noStroke();
  rect(10, 10, 100, 100);
  
  // Mostrar información en pantalla
  fill(255);
  textSize(14);
  text("Píxel en (100, 100)", 10, 130);
  text("R: " + int(r), 10, 150);
  text("G: " + int(g), 10, 170);
  text("B: " + int(b), 10, 190);
  text("Hex: #" + hex(c, 6), 10, 210);
}
