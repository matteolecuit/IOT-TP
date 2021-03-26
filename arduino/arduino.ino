#define LED 13
#define LUM A1

int state = HIGH;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(LUM, INPUT);
}

void loop() {
  String test = "{ 'lumen' : ";
  String json = test + analogRead(LUM);
  String json2 = json + "}";
  digitalWrite(LED, state);
  delay(200);
  digitalWrite(LED, !state);
  Serial.print(json2);
  delay(300);
}

void toggle(){
  state = !state;
}
