Balloon t;

void setup() {
  size(500, 500);
  t = new Balloon(200, 200, 70);
}

void draw() {
  background(255);
  t.display();
}

class Balloon {
  float x, y, r;

  Balloon(float x, float y, float r) {
    this.x = x;
    this.y = y;
    this.r = r;
  }

  void display() {
    fill(255, 100, 150);
    stroke(0);
    ellipse(x, y, r, r);
    line(x, y + r / 2, x, y + r / 2 + 40);
  }
}
