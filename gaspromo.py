import MFRC522
import signal
#print "Show Your ID Card"
continue_reading = True
MIFAREReader = MFRC522.MFRC522()


#cardB = [83,164,247,164,164]
#cardC = [20,38,121,207,132]

def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  print "Ctrl+C captured, ending read."
  MIFAREReader.GPIO_CLEEN()

signal.signal(signal.SIGINT, end_read)
price = raw_input("Enter the Price and Show Your Customer Card: ")
while continue_reading:
  (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
  if status == MIFAREReader.MI_OK:
    #print "Card detected"
    (status,backData) = MIFAREReader.MFRC522_Anticoll()
  if status == MIFAREReader.MI_OK:
    #print "Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
    #print str(backData)

    rfId = str(backData)
    getParameters = "http://192.168.1.23/getId.php?id=" + rfId + "&price=" + price

    import requests
    r = requests.get(getParameters)

    print r.content
    price = raw_input("Enter the Price and Show Your Customer Card: ")

