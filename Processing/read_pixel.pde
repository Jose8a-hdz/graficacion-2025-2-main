PImage img;
int blackPixels = 0;

void setup() {
  size(800, 800);
  
  // Cargar imagen desde la carpeta "data"
  img = loadImage("imagen.png");
  img.resize(width, height); // Ajustar al lienzo
  image(img, 0, 0);
  
  // Contar píxeles
  img.loadPixels();  // Acceder al array de píxeles
  blackPixels = 0;
  
  for (int i = 0; i < img.pixels.length; i++) {
    color c = img.pixels[i];
    
    // Extraer valores RGB
    float r = red(c);
    float g = green(c);
    float b = blue(c);
    
    // Definir umbral para considerar "negro"
    if (r < 50 && g < 50 && b < 50) {
      blackPixels++;
    }
  }
  
  println("Total píxeles negros: " + blackPixels);
}

void draw() {
  // Solo muestra la imagen
  image(img, 0, 0);
}
