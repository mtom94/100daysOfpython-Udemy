#TODO-1 Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2 Inside the 'encrypy' function , shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.

#eg
#plain_text = 'hello'
#shift = 5
#cipher_text = 'mjqqt'
#print output: "The encoded text is mjqqt"

#TODO-3 Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

#TODO-4 Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs .
#TODO-5 Inside the 'decrypt' function , shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.

#eg
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output : "The decoded text is hello"

#TODO-6 Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.

#TODO-7 Combine the encrypt() and decrypt () functions into a single function called caesar().

#TODO-8 Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

#TODO-9 Import and print the logo from art.py when the program starts.

#TODO-10 Can you figure out a way to ask the user if they want to restart the cipher program?

#eg - Type "yes" if you want to go again. Otherwise type "no"

#If they type 'yes ' then ask them for the direction/text/shift again and call the caesar() function again?

#Hint: Try creating a neew function that calls itself if they type 'yes'.

#what if the user enters a shift that is greater than the number of letters in the alphabet?

#Try running the program and entering a shift number of 45.

#hint: Think about how you can use the modulus.

#create a 'encrypt' function with input

# def encrypt(plain_text, shift_amount):
# #     cipher_text = ""
# #     for letter in plain_text :
# #         position = alphabet.index(letter)
# #         new_position = position + shift_amount
# #         new_letter = alphabet[new_position]
# #         cipher_text += new_letter
# #     print(f"The encoded text is {cipher_text}")
# # #encrypt(plain_text=text, shift_amount=shift)
# #
# # def decrypt(cipher_text, shift_amount):
# #     plain_text = ""
# #     for letter in cipher_text:
# #         position = alphabet.index(letter)
# #         new_position = position - shift_amount
# #         plain_text += alphabet[new_position]
# #     print(f"The decoded text is {plain_text}")
# #
# # if direction == "encode" :
# #     encrypt(plain_text=text, shift_amount=shift)
# # else:
# #     decrypt(cipher_text=text, shift_amount= shift)

