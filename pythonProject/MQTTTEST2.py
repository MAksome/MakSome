import paho.mqtt.client as paho
import csv
topic="GGEZkmutt"
def on_connect(client, userdata, flags, rc):
    print('CONNACK received with code %d.' %(rc))
    
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(granted_qos))

def on_message(client, userdata, msg):
    message=msg.payload.decode("utf-8")
    print('on message msg.payload=',msg.payload)  #สั่ง print in window
    if not "*" in message:
        mes = message.split(',')
        print(mes)
        #print(msg.payload=='hello')
        if mes [0] == str ('0') :    #แปลงค่า 0 จาก int เป็น  str
            client.publish(topic,'*turnLeft')
        elif mes [2] == str ('0') :
            client.publish(topic,'*forward' )
        if message == 'turnleft':
            client.publish(topic, -90)
        # if message == 'turnRightd':
        #     client.publish(topic, +90)%360
        # if message == 'turnRightd':
        #     client.publish(topic, +90)%360

        # print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
        # temperature = ((msg.topic+" "+str(msg.qos)+" "+str(msg.payload)) )
        # (rc, mid) = client.publish('MQTTkmutt', str(temperature), qos=1)

def on_publish(client, userdata, mid):
    print("client: "+str(client))
    print("userdata: "+str(userdata))
    print("mid: "+str(mid))

client = paho.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('broker.mqttdashboard.com', 1883)
client.subscribe(topic, qos=0)
# client.publish("GGEZkmutt",10)

with open('direction.csv','w',newline='') as csvfile:                               # การเขียนส่วนของ CSV
    spamwriter = csv.writer(csvfile)#,delimiter=',',
  #                          #quotechar='|', quoting=csv.QUOTE_MINIMAL))
    spamwriter.writerow(['Cell' , 'E','W','N','S'])                       #ส่วนของ CSV กำหนดหัวข้อ
    spamwriter.writerow(["(1,1)",'1','0','0','0',])                               #ส่วนของ CSV กำหนดข้อมูล
    spamwriter.writerow(["(2,1)",'1','0','0','0',])
    spamwriter.writerow(["(1,2)",'0','1','0','1',])
    spamwriter.writerow(["(2,2)",'0','1','1','0',])

    with open('directionforc.csv','w',newline='') as csvfile:                               # การเขียนส่วนของ CSV
        spamwriter = csv.writer(csvfile)#,delimiter=',',
  #                          #quotechar='|', quoting=csv.QUOTE_MINIMAL))
        spamwriter.writerow(['X','Y' , 'E','W','N','S'])                       #ส่วนของ CSV กำหนดหัวข้อ
        spamwriter.writerow(['1','1','1','0','0','0',])                               #ส่วนของ CSV กำหนดข้อมูล
        spamwriter.writerow(['2','1','1','0','0','0',])
        spamwriter.writerow(['1','2','0','1','0','1',])
        spamwriter.writerow(['2','2','0','1','1','0',])


# if haveMoney:
#     if hungry:
#         eat()
client.loop_forever()  #loopต้งไว้ท้ายสุดเท่านั้น