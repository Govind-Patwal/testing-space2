# Installing SAP HANA 2.0 express edition on a precongigured VM - https://developers.sap.com/group.hxe-install-vm-xsa.html

# GOOD VIDEO : https://youtu.be/71Z4F5eKR-g

# https://saphanajourney.com/hana-cloud/learning-article/using-jupyter-notebooks-with-sap-hana-cloud/#step-1

### Source: https://developers.sap.com/tutorials/hana-clients-python.html
### https://help.sap.com/viewer/0eec0d68141541d1b07893a39944924e/2.0.02/en-US/f3b8fabf34324302b123297cdbe710f0.html

#Import your dependencies
import platform
from hdbcli import dbapi


#verify the architecture of Python
print ("Platform architecture: " + platform.architecture()[0])

#Initialize your connection
conn = dbapi.connect(
    #Option 1, retrieve the connection parameters from the hdbuserstore
    key='USER1UserKey', # address, port, user and password are retrieved from the hdbuserstore

    #Option2, specify the connection parameters
    #address='10.7.168.11',
    #port='39015',
    #user='User1',
    #password='Password1',

    #Additional parameters
    #encrypt=True, # must be set to True when connecting to HANA as a Service
    #As of SAP HANA Client 2.6, connections on port 443 enable encryption by default (HANA Cloud)
    #sslValidateCertificate=False #Must be set to false when connecting
    #to an SAP HANA, express edition instance that uses a self-signed certificate.
)
#If no errors, print connected
print('connected')

cursor = conn.cursor()
sql_command = "select TITLE, FIRSTNAME, NAME from HOTEL.CUSTOMER;"
cursor.execute(sql_command)
rows = cursor.fetchall()
for row in rows:
    for col in row:
        print ("%s" % col, end=" ")
    print (" ")
cursor.close()
conn.close()