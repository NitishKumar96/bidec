    int LED[5]={0,0,0,0,0}; // initial values for the led
    int IR[5]={0,0,0,0,0};  // initial out put values of ir sensors
    
    int LED_pin[5]={3,5,6,9,10}; // pins to connect the leds
    int IR_pin[5]={A0,A1,A2,A3,A4};   // pins to read the ir
    long timer[5]={0,0,0,0,0};
    long maintimer;

    #include <PinChangeInt.h>

    

    #define p25  5
    #define p50  110
    #define p75 180
    #define p100 255

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
      void setup() {
        
              Serial.begin(9600); // begin the serial monitor
              
                pinMode(LED_pin[0],OUTPUT);// define the output pins for the leds
                pinMode(LED_pin[1],OUTPUT);
                pinMode(LED_pin[2],OUTPUT);
                pinMode(LED_pin[3],OUTPUT);
                pinMode(LED_pin[4],OUTPUT);
                
                pinMode(IR_pin[0],INPUT);// for the proximity sensor
                pinMode(IR_pin[1],INPUT);
                pinMode(IR_pin[2],INPUT);
                pinMode(IR_pin[3],INPUT);
                pinMode(IR_pin[4],INPUT);
               
                 PCintPort::attachInterrupt(IR_pin[0],read_IR0,CHANGE); // attach the interupts for the ir values
                 PCintPort::attachInterrupt(IR_pin[1],read_IR1,CHANGE);
                 PCintPort::attachInterrupt(IR_pin[2],read_IR2,CHANGE);
                 PCintPort::attachInterrupt(IR_pin[3],read_IR3,CHANGE);
                 PCintPort::attachInterrupt(IR_pin[4],read_IR4,CHANGE);  

                  for (int i=0;i<5;i++) LED[i]=p25;
                  ledout();
    
    }
    
    int i; // varible used for the loop
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        // main loop
        
        void loop(){
                
                // finaly write the led values
               ledout();
               
                for(i=0;i<5;i++){
                if (LED[i]!=p25)
                if (millis()-timer[i] >= 2000) LED[i]=p25;
                }

                printdata(); // function to print the running data 
              
              }



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
     void ledout(){ // finally give the output to the leds
                analogWrite(LED_pin[0],LED[0]);
                analogWrite(LED_pin[1],LED[1]);
                analogWrite(LED_pin[2],LED[2]);
                analogWrite(LED_pin[3],LED[3]);
                analogWrite(LED_pin[4],LED[4]); 
     }
    
    
  ///////////////////////////////////////////////////////////////////////////////////////////  //////////////////////////////////////////////////
// folling are the functions for the interupt routine
    
    
    void read_IR0(){       
      LED[0]=p100; timer[0]=millis();
      LED[1]=p100;  timer[1]=millis();
      LED[2]=p75;  timer[2]=millis();
      //ledout();
      }
      
    void read_IR1(){
      LED[0]=p75; timer[0]=millis();
      LED[1]=p100; timer[1]=millis();
      LED[2]=p100;  timer[2]=millis();
      LED[3]=p75;  timer[3]=millis();
      //ledout();

      }
      
    void read_IR2(){
      LED[1]=p75; timer[1]=millis();
      LED[2]=p100; timer[2]=millis();
      LED[3]=p100;  timer[3]=millis();
      LED[4]=p75;  timer[4]=millis();

      }
      
    void read_IR3(){
      LED[2]=p75; timer[2]=millis();
      LED[3]=p100; timer[3]=millis();
      LED[4]=p100;  timer[4]=millis();
      //ledout();

      }
      
    void read_IR4(){
      LED[3]=p75; timer[3]=millis();
      LED[4]=p100; timer[4]=millis();
      //ledout();

      }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void printdata(){    // this function is used to print the running data
  
  
                Serial.print( digitalRead(IR_pin[0]));
                Serial.print(" 0  ");
                Serial.print(LED[0]);
                Serial.print(" ");
                Serial.print(timer[0]);
                Serial.print(":: ");
                
                Serial.print( digitalRead(IR_pin[1]));
                Serial.print(" 1  ");
                Serial.print(LED[1]);
                Serial.print(" ");
                Serial.print(timer[1]);                
                Serial.print(":: ");
                
                Serial.print( digitalRead(IR_pin[2]));
                Serial.print(" 2  ");
                Serial.print(LED[2]);
                Serial.print(" ");
                Serial.print(timer[2]);              
                Serial.print(":: ");
                
                Serial.print( digitalRead(IR_pin[3]));
                Serial.print(" 3  ");
                Serial.print(LED[3]);
                Serial.print(" ");
                Serial.print(timer[3]);              
                Serial.print(":: ");
                
                Serial.print( digitalRead(IR_pin[4]));
                Serial.print(" 4  ");
                Serial.print(LED[4]);
                Serial.print(" ");
                Serial.print(timer[4]);              
                Serial.println(":: ");
  
  }
    
    
    

