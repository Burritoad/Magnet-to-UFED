import zipfile
import tarfile
import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.zip'):
        print("extracting "+file)
        zip_ref = zipfile.ZipFile(file, 'r')
        os.mkdir("UFED")
        zip_ref.extractall("UFED")
        zip_ref.close()
		
print("extracting adb-data.tar")		
tar = tarfile.open("UFED/adb-data.tar")
tar.extractall(path="UFED")
tar.close()

print("Moving Databases")	
if os.path.isfile("UFED/Agent Data/calendar.db"):	
    os.mkdir("UFED/com.android.providers.calendar")
    os.mkdir("UFED/com.android.providers.calendar/db")
    os.rename("UFED/Agent Data/calendar.db", "UFED/com.android.providers.calendar/db/calendar.db")

os.mkdir("UFED/com.android.providers.contacts")
os.rename("UFED/Agent Data/contacts2.db", "UFED/com.android.providers.contacts/contacts2.db")
os.rename("UFED/Agent Data/contacts3.db", "UFED/com.android.providers.contacts/contacts3.db")

if os.path.isfile("UFED/Agent Data/wifi.db"):
    os.mkdir("UFED/com.android.providers.databases")
    os.rename("UFED/Agent Data/wifi.db", "UFED/com.android.providers.databases/wifi.db")

if os.path.isfile("UFED/Agent Data/mmssms.db"):
    os.mkdir("UFED/com.android.providers.telephony")
    os.mkdir("UFED/com.android.providers.telephony/databases")
    os.rename("UFED/Agent Data/mmssms.db", "UFED/com.android.providers.telephony/databases/mmssms.db")
