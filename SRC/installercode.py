void installSoftware() {
  Serial.println("Installatieproces gestart...");
  // Voeg hier installatiecode toe, bijvoorbeeld softwaredownload of configuratie
}

void utilityFunction() {
  Serial.println("Uitvoeren van systeemcontrole...");
  // Voeg hier systeemdiagnostiek of andere nuttige functies toe
}

void setup() {
  Serial.begin(9600);
  installSoftware();  // Start installatieproces
  utilityFunction();  // Start nuttige systeemfunctie
}
