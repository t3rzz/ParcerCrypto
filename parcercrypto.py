import requests
from tkinter import *
from tkinter import messagebox

class MyClass914:
    def __init__(self, master):
        self.root = master
        self.root.resizable(width=False, height=False)
        self.root.title("Парсинг курса криптовалюты - Лежнев 914")
        self.root.geometry("400x300")

        self.lbl = Label(root, text="Введите монету")
        self.lbl.place(x=200, y=50, anchor="c")

        self.field = Entry()
        self.field.place(x=200, y=80, anchor="c")

        self.btn = Button(text="Показать", command=self.main)
        self.btn.place(x=200, y=110, anchor="c")

        self.text = Text(root, height=1, width=15)
        self.text.pack()
        self.text.tag_configure("center", justify='center')
        self.text.place(x=200, y=200, anchor="c")

    def get_data(self, coin):
        r = requests.get(f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=1000").json()
        for element in r['data']['cryptoCurrencyList']:
            if element["name"].lower() == coin.lower() or element['symbol'].lower() == coin.lower():
                coin_price = element['quotes'][0]['price']
                return f"{round(coin_price, 2)} $USD"

    def main(self):
        self.text.delete('1.0', END)
        self.text.insert(END, self.get_data(self.field.get()))

if __name__ == '__main__':
    root = Tk()
    win = MyClass914(root)
    root.mainloop()
