int motion_1 = 2;
int light_1 = 13;
int sent = 3;

int key1_send = 8;
int key1_receiver = 9;
int key2_send = 10;
int key2_receiver = 11;

float tempC;
int reading;
int tempPin = 5;

void setup(){
  Serial.begin(9600);
  analogReference(INTERNAL);
  pinMode (motion_1,INPUT);
  pinMode (light_1, OUTPUT);
  
  pinMode (key1_send,OUTPUT);  
  pinMode (key2_send,OUTPUT);  
  
  pinMode (key1_receiver,INPUT);  
  pinMode (key2_receiver,INPUT);    
  
  Serial.println('!');
}

void loop (){
  delay(1000);
  
  digitalWrite(key1_send,HIGH);          
  digitalWrite(key2_send,HIGH);          
  
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
  
  
  int key1 = digitalRead(key1_receiver);
  int key2 = digitalRead(key2_receiver);  
  
  if (key1==HIGH)
  {
    Serial.println("key1 1");
  }
  else
  {
    Serial.println("key1 0");
  }
  
  if (key2==HIGH)
  {
    Serial.println("key2 1");
  } 
  else 
  {
    Serial.println("key2 0");    
  }
  
}
