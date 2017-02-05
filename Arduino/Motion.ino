int motion_1 = 2;
int light_1 = 13;
int sent = 3;

float tempC;
int reading;
int tempPin = 5;

void setup(){
  Serial.begin(9600);
  analogReference(INTERNAL);
  pinMode (motion_1,INPUT);
  pinMode (light_1, OUTPUT);
  
  Serial.println('!');
}

void loop (){
  delay(1000);
  
  reading = analogRead(tempPin);
  tempC = reading / 9.31;
  Serial.print("temp ");
  Serial.println(tempC);
  
  int sensor_1 = digitalRead(motion_1);
  if (sensor_1 == HIGH){
      Serial.println("motion");
      digitalWrite(light_1,HIGH);          
  }
  else
  {
      Serial.println("nomotion");      
      digitalWrite(light_1,LOW);       
  }
}
