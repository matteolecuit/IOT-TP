#define ledPin 13
#define lumPin A1

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(lumPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

int val = HIGH;
int s = 0;

void loop() {
  String json1 = "{ \"lumen\" : ";
  String json4 = json1 + analogRead(lumPin);
  Serial.println(json4 + "}");

  digitalWrite(ledPin, val);
  delay(200);
  digitalWrite(ledPin, !val);
  
  delay(1000);
  
  if (Serial.available() > s) {
    toggle_val();
    s = Serial.available();
  }
}

void toggle_val(){
  val = !val;
}
