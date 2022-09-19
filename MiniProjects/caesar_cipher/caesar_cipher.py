
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end=False


#---Defining a finction cipher.
def cipher(text,shift,direction):

    #TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
        encoded_text=[]   #creating a list of encoded text
        decoded_text=[]   # creating list of decoded text
        for char in text:
            if char in alphabet:                   # for each char in text we cheacking its position in the list of alphabet
                position=alphabet.index(char)
                if (position+shift)>26:                # we cheacking shift + position is >26 then we adjust the shift accordingly
                    new_position=(position+shift)-26
                    encoded_text+=alphabet[new_position]  # adding shifted char to list of encoded or decoded
                else:
                    encoded_text+=alphabet[shift+position]
                decoded_text+=alphabet[position-shift]
            else:
                encoded_text+=char
                decoded_text+=char
        if direction=="encode":
            print(f"The encoded text is {''.join(encoded_text)}")   #  
        if direction=="decode":                                     #  converting the list in text and printing them
            print(f"The encoded text is {''.join(decoded_text)}")   # 







while not end:                #---Here started loop for asking for encode and decode again and again.
    direction1 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()    
    text1 = input("Type your message:\n").lower()                                          
    shift1 = int(input("Type the shift number:\n"))                                      

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    
    
    shift1=shift1%26

    cipher(text=text1,shift=shift1,direction=direction1) # calling the function
    x=input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if x=="yes":
        end=False
    else:
        end=True











#initial code written by me
""" def decrypt(text,shift):
    decoded_text=[]
    for letters in text:
        position=alphabet.index(letters)
        decoded_text+=alphabet[position-shift]
    print(f"The decoded text is {''.join(decoded_text)}") """

""" if direction=="encode":
    encrypt(text=text1,shift=shift1)
if direction=="decode":
    decrypt(text=text1,shift=shift1) """