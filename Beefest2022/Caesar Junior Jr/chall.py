#HEY, I'M JULIUS JUNIOR JR.

def encrypt(text,s):
  final_result= ""
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
      final_result += chr((ord(char) + s-65) % 26 + 65)
    elif (char.islower()):
      final_result += chr((ord(char) + s - 97) % 26 + 97)
    elif (char.isnumeric()):
      final_result += chr((ord(char) + s - 48) % 10 + 48)
    else:
      final_result += char
  return final_result

text = ""
shift = 3
expected = "EHHFWI{3k_vw4oo_f7qw_diw6u_k6a_f7hvdu_f7hvdu_keq1543}"
text = input("NOOT NOOT!\nWhat's the General passcode?\n") #input here.
if(expected == encrypt(text,shift)):
    print("Yay You got the flag! WooHoo!")
    print(encrypt(text,shift))
else:
    print("Better luck next time! :)")
    print(encrypt(text,shift))