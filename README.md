# hand-gesture-controlled-electronic-devices
Using hand gestures to control electronic devices using raspberry pi (without external camera). Camera of the PC is used to detect the gesture and raspberry py is used to controll the output.

### Setup

1. Copy PC's public key to Raspberry Pi's authorized keys ( ~/.ssh/authorized_keys ) to be able to ssh without password

2. Move Raspberry Pi's code to raspberry to pi

3. run "python hand_gesture.py"

(Note: I have averaged out the gesture to reduce error , so an average of 3 and above is fast and less than 3 is slow/low)

For demo purpose I have controlled LED attached to Raspberry Pi's GPIO (pin number 15)


Hand gesture code is tweaked from repo https://github.com/sashagaz/Hand_Detection
