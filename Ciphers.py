#  File: Ciphers.py
#  Description: HW12: Substitution Ciphers
#  Student's Name: Austin Keith Faulkner    
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#
#  Date Created: November 1, 2019
#  Date Last Modified: November 7, 2019 (3:56 pm)


def encode(key, plaintext):

    keyCapitalize = list(key.upper())
    key = list(key)
    
    plaintext = list(plaintext)
    cipherTextBuild = []

    LOWERCASE_UPPERCASE_DIFFERENCE = 32
    
    for i in range(len(plaintext)):
        cipherTextBuild.append("")

   
    for lowerCaseLetterNum in range(ord('a'), ord('z') + 1):
        for i in range(len(plaintext)):
            if plaintext[i] == chr(lowerCaseLetterNum):
                cipherTextBuild[i] = key[lowerCaseLetterNum - ord('a')]
            elif plaintext[i] == chr(lowerCaseLetterNum - LOWERCASE_UPPERCASE_DIFFERENCE):
                cipherTextBuild[i] = keyCapitalize[lowerCaseLetterNum - ord('a')]
            elif (ord(plaintext[i]) < ord('A')) or (ord('Z') < ord(plaintext[i]) < ord('a')) or (ord(plaintext[i]) > ord('z')):
                cipherTextBuild[i] = plaintext[i]
            elif plaintext[i] == "":
                return None
            
                                                                                       
    encodedString = " "

    for i in range(len(plaintext)):    
        encodedString += cipherTextBuild[i]
                                                                                            
    return encodedString


def decode(key, ciphertext):

    keyCapitalize = list(key.upper())
    key = list(key)
    
    ciphertext = list(ciphertext)
    revealText = []
    
    for i in range(len(ciphertext)):
        revealText.append("")

   
    for i in range(len(key)):
        for j in range(len(ciphertext)):
            if key[i] == ciphertext[j]:
                revealText[j] = chr(ord('a') + i)  
            elif keyCapitalize[i] == ciphertext[j]: 
                revealText[j] = chr(ord('A') + i)
            elif (ord(ciphertext[j]) < ord('A')) or (ord('Z') < ord(ciphertext[j]) < ord('a')) or (ord(ciphertext[j]) > ord('z')):
                revealText[j] = ciphertext[j]
            elif ciphertext[j] == "":
                return None
            
                                                                                       
    decodedString = " "

    for i in range(len(ciphertext)):    
        decodedString += revealText[i]
                                                                                            
    return decodedString



def main():

    plaintextMessages = [
        ["This is the plaintext message.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Let the Wookiee win!",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Baseball is 90% mental. The other half is physical.\n\t\t- Yogi Berra",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["I used to think I was indecisive, but now I'm not too sure.",
         "mqncdaigyhkxflujzervptobws"],
        ["Einstein's equation 'e = mc squared' shows that mass and\n\t\tenergy are interchangeable.",
         "bludcmhojaifxrkzenpsgqtywv"] ]

    codedMessages = [
        ["Uijt jt uif dpefe nfttbhf.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Qnhxgomhqm gi 10% bnjd eho 90% omwlignh. - Zghe Xmy",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Ulj njxu htgcfj C'gj jgjm mjfjcgjt cx, 'Ep pej jyxj veprx rlhu\n\t\t uljw'mj tpcez jculjm'. - Mcfvw Zjmghcx",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["M 2-wdme uxc yr kylc ua xykd m qxdlcde, qpv wup cul'v gmtd mlw\n\t\t vuj aue yv. - Hdeew Rdyladxc",
         "mqncdaigyhkxflujzervptobws"] ]

    for i in range(len(plaintextMessages)):
        encodedText = encode(plaintextMessages[i][1], plaintextMessages[i][0])
        print("plaintext:   " + plaintextMessages[i][0])
        print("encoded:    " + encodedText)
        decodedText = decode(plaintextMessages[i][1], encodedText)
        print("re-decoded:" + decodedText)
        print()

    for i in range(len(codedMessages)):
        decodedText = decode(codedMessages[i][1], codedMessages[i][0])
        print("encoded:  " + codedMessages[i][0])
        print("decoded: " + decodedText)
        print()

main()
