#include <IRremote.h>

IRsend irsend;

void setup()
{

}

void loop() {
  int khz = 32;
  unsigned int irSignal1[] = {200,1850,250,800,200,1850,250,1900,200,800,200,850,250,800,200,1900,200,800,200,1900,200,850,200,800,200,850,200,1850,250,850,200};
  unsigned int irSignal2[] = {250,1850,200,800,250,1850,250,1800,250,800,250,1850,200,800,250,800,250,1800,250,800,250,1850,200,1850,250,800,250,800,200,1850,250};
  unsigned int irSignal3[] = {250,1800,250,800,250,1850,200,1850,250,800,250,800,200,1850,250,1800,250,850,200,1850,200,800,250,800,250,1850,200,1850,250,800,250};
  unsigned int irSignal4[] = {200,1900,150,900,150,1900,150,1950,150,900,150,1900,150,850,250,850,150,1900,200,850,150,1950,150,1950,250,750,150,850,200,1900,200};
  unsigned int irSignal5[] = {250,1800,300,750,300,1800,250,1800,200,850,150,900,250,1800,200,1850,200,900,150,1900,200,850,200,750,300,1850,200,1900,200,850,150};


  irsend.sendRaw(irSignal1, sizeof(irSignal1) / sizeof(irSignal1[0]), khz); 
  delay(50);
  irsend.sendRaw(irSignal2, sizeof(irSignal1) / sizeof(irSignal2[0]), khz); 
  delay(50);
  irsend.sendRaw(irSignal3, sizeof(irSignal1) / sizeof(irSignal3[0]), khz); 
  delay(50);
  irsend.sendRaw(irSignal4, sizeof(irSignal1) / sizeof(irSignal4[0]), khz); 
  delay(50);
  irsend.sendRaw(irSignal5, sizeof(irSignal1) / sizeof(irSignal5[0]), khz); 

  delay(1000); 
}
