#include <dht.h>
#include <SoftwareSerial.h>

#define dht_dpin 4 //no ; here. Set equal to channel sensor is on

SoftwareSerial bt (8, 9);  //RX, TX (Switched on the Bluetooth - RX -> TX | TX -> RX)
int LEDPin = 13; //LED PIN on Arduino
int btdata; // the data given from the computer

dht DHT;

float humidity = 0.0;
float temperature = 0.0;

void detect_tem_humi(){
  DHT.read11(dht_dpin);

  Serial.print("Current humidity = ");
  Serial.print(DHT.humidity);
  Serial.print("%  ");
  Serial.print("temperature = ");
  Serial.print(DHT.temperature);
  Serial.println("C  ");

  humidity = DHT.humidity;
  temperature = DHT.temperature;

  delay(800);
}

void connect_bluetooth() {

  if (bt.available()) {
    btdata = bt.read();
    if (btdata == '1') {
      //if 1
      digitalWrite (LEDPin, HIGH);
      bt.println ("LED ON!");
    }
    if (btdata == '0') {
      //if 0
      digitalWrite (LEDPin, LOW);
      bt.println ("LED OFF!");
    }
  }
  delay (100); //prepare for data
}

int cnt = 0;

void print_humi_tem() {

//  bt.print("Humidity : ");
  bt.print(humidity);
//  bt.print(" % ,");
//  bt.print("Temperature : ");
//  bt.print(temperature);
//  bt.print(" C");
  bt.print("\n");

  if (cnt == 5) {
    bt.print("----------------------------------------");
    bt.print("\n");
    Serial.println("---------------------------------------");
    cnt = 0;
  }
  cnt++;
}

void setup() {
  bt.begin(9600);
  bt.println ("Bluetooth ON. Press 1 or 0 to blink LED..");
  pinMode (LEDPin, OUTPUT);

  Serial.begin(115200);
  delay(300);//Let system settle
  Serial.println("Humidity and temperature\n\n");
  delay(700);
}
//Wait rest of 1000ms recommended delay before
//accessing sensor
//end "setup()"



void loop() {
  //This is the "heart" of the program.

  connect_bluetooth();

  detect_tem_humi();

  print_humi_tem();
}

//Don't try to access too frequently... in theory
//should be once per two seconds, fastest,
//but seems to work after 0.8 second.
// end loop()

