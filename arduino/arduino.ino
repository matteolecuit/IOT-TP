#define ledPin 13
#define lumPin A1

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(lumPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

int val = HIGH;

void loop() {
  String json1 = "{ \"lumen\" : ";
  String json4 = json1 + analogRead(lumPin);
  Serial.println(json4 + "}");

  digitalWrite(ledPin, val);
  delay(200);
  digitalWrite(ledPin, !val);
  
  delay(300);

  if (Serial.available() > 0) {
    String data = Serial.readString();
    Serial.print("You sent me: ");
    Serial.println(data);
    toggle_val();
  }
}

void toggle_val(){
  val = !val;
}
