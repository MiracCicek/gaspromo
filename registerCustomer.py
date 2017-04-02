import MFRC522
import signal
import MySQLdb

continue_reading = True
MIFAREReader = MFRC522.MFRC522()
def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  print "Ctrl+C captured, ending read."
  MIFAREReader.GPIO_CLEEN()
signal.signal(signal.SIGINT, end_read)
nameSurname = raw_input("Enter Name and Surname :")
dateOfBirth = raw_input("Enter Date Of Birth (DD/MM/YYYY) :")
mailAddress = raw_input("Enter E-Mail Address :")
phoneNumber = raw_input("Enter Phone Number (905052996953) :")
city		= raw_input("Enter City Name")
homeAddress = raw_input("Enter Home Address :")
carPlate	= raw_input("Enter Plate Number :")

sqlQuery = "INSERT INTO musteriler (adSoyad, dogumtarihi, telefon, adres, mail, plaka, aktif, sehir) VALUES ('" #+ nameSurname + "','" + $dateOfBirth + "','" + phoneNumber +"','" +homeAddress + "', '" + mailAddress + "', '" + carPlate + ", 1, '" + city + "')"
print sqlQuery
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="352458",  # your password
                     db="gasprom")
cur = db.cursor()
cur.execute(sqlQuery)
db.commit()

cur.close()
db.close()
