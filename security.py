from backend import hash
import random

class hillCipher:
    def __init__(self, key):
        self.genTable()
        self.arr_size=len(self.arr)
        self.key = self.CharToIntTable(hash(key))
    
    def genSalt(self):
        salt_len = random.randint(200,400)
        salt = []
        for i in range(salt_len):
            indexTable = random.randint(0,self.arr_size-2)
            salt.append(self.arr[indexTable])
        salt.append('e8605470426611edb8780242ac120002')
        return "".join(salt)
    
    def genTable(self):
        self.arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"," ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "'", ";", ":", "<", ">", "?", "+", "_", "~"]
        return

    def CharToIntTable(self, data):
        dataI = [self.arr.index(letter) for letter in data]
        return dataI
    
    def IntToCharTable(self, text):
        data = [self.arr[i] for i in text]
        return "".join(data)
     
    def encrypt(self, data):
        salt = self.genSalt()
        print('satl', salt)
        data = f"{salt}{data}"
        data = self.CharToIntTable(data)
        key_length = len(self.key)
        
        cipher = []
        ind_key = 0
        for m in data:
            data_cipher = (m + self.key[ind_key]) % self.arr_size
            cipher.append(data_cipher)
            ind_key = 0 if ind_key + 1 == key_length else ind_key + 1

        print('cipherText number', cipher)
        cipherText = self.IntToCharTable(cipher)
        return cipherText
    
    def decrypt(self, cipherText):
        try:
            cipherC = self.CharToIntTable(cipherText)
            key_length = len(self.key)

            plaint = []
            ind_key = 0
            for m in cipherC:
                data_plaint = (m - self.key[ind_key]) % self.arr_size
                plaint.append(data_plaint)
                ind_key = 0 if ind_key + 1 == key_length else ind_key + 1
            
            print('Plaintext number', plaint)
            plaintText = self.IntToCharTable(plaint)
            plaintText = plaintText.split('e8605470426611edb8780242ac120002')[-1]

            return plaintText
        except:
            return '<this is not your result> !! something error!'