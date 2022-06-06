alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']#defining all letters in the alphabet
def entry():
    word=input("enter the word")#asks the user to enter the string
    shift=int(input("enter the shift"))#asks the user to enter the shift
    data=(word,shift)
    data=(word.lower(),shift)
    return(data)#returs both the shift and the word

    
def encrypt(word,shift):#encrypts the word
    word=word.lower()
    encrypted=""
    for letter in word:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=(position+shift)%26
            encrypted+=alphabet[new_position]
        
        else:
            encrypted+=letter
    print(encrypted)
    return encrypted
def decrypt(word,shift):#decrypts the word
    word=word.lower()
    decrypted=""
    for letter in word:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=(position-shift)%26
            decrypted+=alphabet[new_position]
        
        else:
            decrypted+=letter
    print(decrypted)
    return decrypted
def main():#asks the user to make a choice
    try_it=True
    while try_it==True:
        print("Make code\n")
        print("1.Encrypt\n")
        print("2.Decrypt\n")
        print("3.Exit\n")
        choice=int(input("enter the choice"))
        if choice==1:
            (word,shift)=entry()
            encrypt(word,shift)
        elif choice==2:
            (word,shift)=entry()
            decrypt(word,shift)
        elif choice==3:
            try_it=False
            exit()

main()