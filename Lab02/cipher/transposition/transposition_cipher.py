class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key
        return ''.join(ciphertext)

    def decrypt(self, text, key):
        num_of_rows = key
        num_of_cols = int(len(text) / key) + (len(text) % key > 0)
        num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(text)

        plaintext = [''] * num_of_cols
        col = 0
        row = 0

        for symbol in text:
            plaintext[col] += symbol
            col += 1
            if col == num_of_cols or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
                col = 0
                row += 1

        return ''.join(plaintext)
