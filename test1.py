
import pymongo
client = pymongo.MongoClient("mongodb+srv://Likith422:Likibenki@likith422.mpteby8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data = {
    "name" : "likithtn" ,
    "mail_id" : "likith422p@gmail.com" ,
    "subject" : ["data science" , "big data" , "data analytics"]
}

list_of_records = [
    {"companyName" : "sriGuru" ,
     "product" : "pvc" ,
     "courseOffered" : "machine learning with development"} ,

    {"companyName" : "sriGuru" ,
     "product" : "pvc" ,
     "courseOffered" : "deep learning for NLP computer vision"} ,

    {"companyName" : "sriGuru" ,
     "product" : "master program" ,
     "courseOffered" : "data science master program"}
]

database  = client['myinfo']
collection = database['liki']
#collection.insert_one(data)
collection.insert_many(list_of_records)

collection1 = database["dpkt"]
data1 = {"packetType": "D",
          "data": {"checkEngineLightFlag": "F", "batteryVoltageStableTime": 0, "batteryVoltageStable": "0",
                   "batteryVoltageOff": "12.42", "batteryCrankParamTN": "-0.08", "batteryCrankParamVN": "0.00",
                   "batteryCrankParamTP": "-0.08", "batteryCrankParamVP": "0.00", "batteryCrankParamTT": "-0.00008",
                   "batteryCrankParamV0": "0.00", "batteryVoltageMaxOn": "13.05", "batteryVoltageMinOn": "12.97",
                   "batteryVoltageMaxOff": "12.46", "batteryVoltageMinOff": "12.36", "batteryVoltageOnAverage": "13.02",
                   "engineLoadMax": "84", "engineLoadAverage": "39.98", "rpmMax": "3487", "rpmAverage": "1431.29",
                   "gpsSpeedAverage": "21.99", "vssMax": "53.44", "vssAverage": "23.06", "tcuTemperatureMin": "82.40",
                   "tcuTemperatureMax": "109.40", "tcuTemperatureAverage": "104.87", "coolantMin": "158.00",
                   "coolantMax": "188.60", "coolantAverage": "180.20", "packetStartLocal": 1508143346000,
                   "tripStartLocal": 1508143346000, "milIndicator": "F", "monitorsNotReady": 0, "imei": "60DF5417",
                   "gatewayTs": 1515613306592, "diagnosticTroubleCodeData": [],
                   "diagnosticPidData": [[64768, 47, 100], [64768, 1, 517376], [64800, 1, 262144], [64768, 5, 125]]},
          "header": {"iwrapVer": "1.9.20", "sourceSystem": "CDP", "configVer": "1.1", "oemName": "HUM", "unitType": 0,
                     "cpVer": "7.50.1.9", "igpsVer": "1.3.7", "messageType": "Notification", "pomVer": "1.0",
                     "headerVer": "V6", "timestamp": 0, "deviceType": "InDrive", "visorVer": "1.4.35",
                     "transactionId": "53098471-7787-4160-94b3-cd69dcc70416", "deviceSerialNo": "60DF5417",
                     "subOrganization": "HUM", "organization": "HUM", "imei": "60DF5417", "operation": "Notification"}}

collection1.insert_one(data1)

record = collection.find()
for i in record:
    print(i)









