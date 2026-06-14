#include <DHT.h>

#define MQ135_PIN 34

#define DHTPIN 4
#define DHTTYPE DHT22

#define LED_PIN 2
#define BUZZER_PIN 15

DHT dht(DHTPIN, DHTTYPE);

String classifyAQI(int value)
{
  if(value <= 100)
      return "GOOD";

  else if(value <= 200)
      return "MODERATE";

  else if(value <= 350)
      return "POOR";

  else
      return "HAZARDOUS";
}

void setup()
{
  Serial.begin(115200);

  dht.begin();

  pinMode(
      LED_PIN,
      OUTPUT
  );

  pinMode(
      BUZZER_PIN,
      OUTPUT
  );
}

void loop()
{
  int airValue =
      analogRead(MQ135_PIN);

  float temperature =
      dht.readTemperature();

  float humidity =
      dht.readHumidity();

  String status =
      classifyAQI(airValue);

  Serial.println(
      "--------------------"
  );

  Serial.print(
      "Air Quality: "
  );

  Serial.println(
      airValue
  );

  Serial.print(
      "Temperature: "
  );

  Serial.println(
      temperature
  );

  Serial.print(
      "Humidity: "
  );

  Serial.println(
      humidity
  );

  Serial.print(
      "Status: "
  );

  Serial.println(
      status
  );

  if(
      status == "POOR" ||
      status == "HAZARDOUS"
  )
  {
      digitalWrite(
          LED_PIN,
          HIGH
      );

      tone(
          BUZZER_PIN,
          1000
      );
  }
  else
  {
      digitalWrite(
          LED_PIN,
          LOW
      );

      noTone(
          BUZZER_PIN
      );
  }

  delay(5000);
}