class hillCipher:
    def __init__(self, key):
        self.genTable()
        self.arr_size=len(self.arr)
        self.key = self.CharToIntTable(key)
        self.data = ""
        
    def genTable(self):
        self.arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q ", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q ", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "'", "\"", ";", ":", "<", ">", "?", "/", "[", "]", "{", "}", "\\", "|"]
        return

    def CharToIntTable(self, data):
        dataI = [self.arr.index(letter) for letter in data]
        return dataI
    
    def IntToCharTable(self, text):
        data = [self.arr[i] for i in text]
        return "".join(data)
    
    def Data(self, data):
        self.data = self.CharToIntTable(data)
        
    def encrypt(self):
        key_length = len(self.key)
        
        cipher = []
        ind_key = 0
        for m in self.data:
            data_cipher = (m + self.key[ind_key]) % self.arr_size
            cipher.append(data_cipher)
            ind_key = 0 if ind_key + 1 == key_length else ind_key + 1
        
        cipherText = self.IntToCharTable(cipher)
        return cipherText
    
    def decrypt(self, cipherText):
        cipherC = self.CharToIntTable(cipherText)
        key_length = len(self.key)

        plaint = []
        ind_key = 0
        for m in cipherC:
            data_plaint = (m - self.key[ind_key]) % self.arr_size
            plaint.append(data_plaint)
            ind_key = 0 if ind_key + 1 == key_length else ind_key + 1
        
        plaintText = self.IntToCharTable(plaint)
        return plaintText

string = 'Aatnbxcs123%^&'
key = 'Tpzhxfc'
hill = hillCipher(key=key)
hill.Data(string)

cipher = hill.encrypt()
plaint = hill.decrypt(cipher)
print("ciphertext ",cipher)
print("plaint ",plaint)