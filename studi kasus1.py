#STUDI KASUS
#Stack  untuk membalik kata
kata = input ("Masukkan kata: ")
stack = []
for huruf in kata:
    stack.append(huruf)
hasil = ""
while stack:
    hasil += stack.pop()

print("Kata dibalik:", hasil)
