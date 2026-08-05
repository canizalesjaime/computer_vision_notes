#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);

void setup() {
  Serial.begin(115200);

  while (!Serial);

  Serial.println("Initializing BNO055...");

  if (!bno.begin()) {
    Serial.println("ERROR: No BNO055 detected!");
    Serial.println("Check wiring and I2C address.");
    while (1);
  }

  delay(1000);

  // Use external crystal if available
  bno.setExtCrystalUse(true);

  Serial.println("BNO055 Ready!");
  Serial.println();
}

void loop() {

  imu::Vector<3> euler =
      bno.getVector(Adafruit_BNO055::VECTOR_EULER);

  Serial.print("Yaw(z): ");
  Serial.print(euler.x());
  Serial.print("°   ");

  Serial.print("Pitch(y): ");
  Serial.print(euler.y());
  Serial.print("°   ");

    Serial.print("Roll(x): ");
  Serial.print(euler.z());
  Serial.println("°   ");

  delay(100);
}