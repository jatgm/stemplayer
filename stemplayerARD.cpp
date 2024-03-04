// C++ code
//
int Inputs[4] = {A0, A1, A2, A3};
int sliderValues[4];

void setup()
{
  for (int i = 0; i < 4; i++) {
    pinMode(Inputs[i], INPUT);
  }
  Serial.begin(9600);
}

void loop()
{
  updateSliderValues();
  printValues();
  //Serial.println(map(analogRead(A0), 0, 1023, 0, 100));
  delay(5);
}

void updateSliderValues() {
	for (int i = 0; i < 4; i++) {
    	sliderValues[i] = map(analogRead(Inputs[i]), 0 , 1023, 0, 100);
  }
}

void printValues() {
  String builtString = String("");

  for (int i = 0; i < 4; i++) {
    builtString += String((int) sliderValues[i]);

    if (i < 4 - 1) {
      builtString += String("|");
    }
  }
  
  Serial.println(builtString);
}
