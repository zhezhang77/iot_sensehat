# iot_sensehat
 **IoT sense hat example**

# Command
* iot_pub_sensehat.py  
  + Publish temperature and humidity data to AWS broker.  
  + **Topic:** iot/temperature, iot/humidity  
  + Press joystick **middle** to exit the program

* iot_sub_sensehat.py  
  + Subscribe to above topics to receive data  
  + Press joystick **left/right** to switch display from Temperature/Humidity/Off  
  + Press joystick **up/down** to exit the program

# TLS certificates
<html><table>
<tr><td> CARoot.pem </td><td> CA file </td></tr>
<tr><td> 66321288b3-certificate.pem.crt </td><td> Client Certificate file </td></tr>
<tr><td> 66321288b3-public.pem.key </td><td> Client Public Key (unused for client) </td></tr> 
<tr><td> 66321288b3-private.pem.key </td><td> Client Private Key </td></tr>
</table></html>

# Broker Info
<html><table>
<tr><td> Server </td><td> a1zd8y5etgd1ze.iot.ap-northeast-1.amazonaws.com  </td></tr>
<tr><td> Port </td><td> 8883 </td></tr>
</table></html>
