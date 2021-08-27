

#define CONTROL_PIN (2)
#define REMOTE_PIN (5)

int remoteState = 0;
int spamProtection = 0;

void toggle_kvm() {
  digitalWrite(CONTROL_PIN, LOW);
  delay(500);
  digitalWrite(CONTROL_PIN, HIGH);
}

void flush_serial() {
  //clear out the serial buffer
  byte w = 0;

  for (int i = 0; i < 10; i++)
  {
    while (Serial.available() > 0)
    {
      char k = Serial.read();
      w++;
      delay(1);
    }
    delay(1);
  }
}

void setup() {
  // open the serial port:
  Serial.begin(9600);

  pinMode(CONTROL_PIN, OUTPUT);
  pinMode(REMOTE_PIN, INPUT_PULLUP);
  digitalWrite(CONTROL_PIN, HIGH); // default to high
  toggle_kvm(); // need to toggle because PC provides power (perhaps get cable and cut power cord?)

  flush_serial();
}

void loop() {
  remoteState = digitalRead(REMOTE_PIN);

  if (spamProtection && remoteState == HIGH) {
    spamProtection = 0; // reset protection because button is released
    delay(300); // to prevent accidental triggers after button release  
  }
  
  // check if remote triggered KVM switch
  else if (!spamProtection && remoteState == LOW) {
    toggle_kvm();
    delay(300); // to prevent spam switch
    spamProtection = 1;
  }
  
  // check for incoming serial data:
  if (Serial.available() > 0) {
      flush_serial();
      toggle_kvm();
      flush_serial();  
  }
}
