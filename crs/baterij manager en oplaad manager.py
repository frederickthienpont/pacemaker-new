// Simuleer batterijpercentage
int batteryLevel = 100; // Start op 100%

// Pin voor de batterijstatus (simulatie)
const int batteryPin = A0; // Verbind een sensor om het batterijniveau te meten

void setup() {
  Serial.begin(9600);
  pinMode(batteryPin, INPUT);
}

void loop() {
  // Simuleer batterijpercentage
  batteryLevel = analogRead(batteryPin) / 10; // Verdeel de input om een percentage te krijgen

  // Print het batterijpercentage naar de seriële monitor
  Serial.print("Batterij percentage: ");
  Serial.println(batteryLevel);

  // Als de batterij op 70% staat, geef een waarschuwing
  if (batteryLevel <= 70) {
    warningBattery();
  }

  delay(5000); // Wacht 5 seconden voor de volgende meting
}

void warningBattery() {
  Serial.println("Waarschuwing: Batterij op 70%! Tijd om op te laden.");
}
