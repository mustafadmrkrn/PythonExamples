
sehirler = ["kocaeli", "istanbul"]
plakalar = [41, 34]

print(plakalar[sehirler.index("kocaeli")]) # s�ral� oldu�u i�in ayn� index numaras�yla yazabildik.

plakalar = {"istanbul" : 34, "kocaeli" : 41}
print(plakalar["istanbul"])

plakalar["ankara"] = 6
print(plakalar)

users = {
"Sema �nal" : 
 {"age" :35,
 "roles": ["admin", "user"],
  "email": "semainal35@gmail.com",
  "address": "izmir",
  "phone" : 5443217307 
 },

 "Tolga �nal":
 {"age": 35,
 "roles": ["user"],
 "email": "inal.tolga@gmail.com",
 "address": "istanbul",
 "phone": 5443217308
 }
}


print(users["Sema �nal"]["roles"])