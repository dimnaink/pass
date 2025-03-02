import random
simvol="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len=int(input("длина пороля"))
gpass=""
for i in range(len):
    gpass+=random.choice(simvol)
print("Сгенирирован пороль",gpass)
