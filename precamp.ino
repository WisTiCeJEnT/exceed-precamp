#define ZXLED 5
#define SWT 6
//int a;
int s;
void setup() {
  //a = 1;
  s = 1;
  pinMode(ZXLED, OUTPUT);
  pinMode(SWT, INPUT);
  Serial.begin(9600);
}


void loop() {
  s = digitalRead(SWT);
  if(s == 0)
  {
    digitalWrite(ZXLED, 1);
    Serial.println("PRESS !");
  }
  else
  {
    digitalWrite(ZXLED, 0);
  }
  delay(300);
  /*
  digitalWrite(ZXLED, HIGH);   
  delay(3000);                      
  digitalWrite(ZXLED, LOW);   
  delay(2000);*/
  
}
