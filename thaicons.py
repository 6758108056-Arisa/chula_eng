import tkinter as tk
import random

# List of Thai consonants with their names
thai_consonants = [
    ("ก", "Gor Gai (กอ ไก่)"),
    ("ข", "Khor Khai (ขอ ไข่)"),
    ("ค", "Khor Khwai (คอ ควาย)"),
    ("ง", "Ngor Ngu (งอ งู)"),
    ("จ", "Jor Jaan (จอ จาน)"),
    ("ช", "Chor Chang (ชอ ช้าง)"),
    ("ต", "Tor Tao (ตอ เต่า)"),
    ("ป", "Por Pla (ปอ ปลา)"),
    ("ฟ", "For Fan (ฟอ ฟัน)"),
    ("ม", "Mor Ma (มอ ม้า)"),
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.card_frame = tk.Frame(root, width=300, height=200)
        self.card_frame.pack_propagate(False)
        self.card_frame.pack(pady=50)
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white", width=6, height=3, relief="solid")
        self.label.pack(expand=True, fill="both")
        
        self.button = tk.Button(root, text="Next Card", command=self.show_new_card, font=("Arial", 14))
        self.button.pack()
        
        self.card_flipped = False
        self.current_card = None
        
        self.label.bind("<Button-1>", self.flip_card)
        self.show_new_card()
    
    def show_new_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0], font=("Arial", 50))
        self.card_flipped = False
    
    def flip_card(self, event):
        if not self.card_flipped:
            self.label.config(text=self.current_card[1], font=("Arial", 20))
            self.card_flipped = True
        else:
            self.label.config(text=self.current_card[0], font=("Arial", 50))
            self.card_flipped = False

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()
