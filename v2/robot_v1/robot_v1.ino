int leftDirPin = 4;
int leftSpeedPin = 5;
int rightDirPin = 7;
int rightSpeedPin = 6;
int runSpeed = 50;

void setupMotorShield()
{
  pinMode(leftDirPin, OUTPUT);
  pinMode(leftSpeedPin, OUTPUT); 
  pinMode(rightDirPin, OUTPUT); 
  pinMode(rightSpeedPin, OUTPUT);
}


void go()
{
  analogWrite(leftSpeedPin, runSpeed);
  analogWrite(rightSpeedPin, runSpeed);
}


void stop()
{
  analogWrite(leftSpeedPin, 0); 
  analogWrite(rightSpeedPin, 0);
}


void goForward()
{
  digitalWrite(leftDirPin, HIGH);
  digitalWrite(rightDirPin, HIGH);
  go();
}


void turnLeft()
{
  digitalWrite(leftDirPin, LOW);
  digitalWrite(rightDirPin, HIGH);
  go();
}


void turnRight()
{
  digitalWrite(leftDirPin, HIGH);
  digitalWrite(rightDirPin, LOW);
  go();
}

void setup()
{
  setupMotorShield();
}

void loop()
{
  goForward();
  delay (2000);
  turnRight();
  delay (500);
  goForward();
  delay(1000);
  turnLeft();
  delay(500);
  stop();
  delay(1000);
}