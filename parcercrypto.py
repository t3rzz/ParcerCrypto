from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import messagebox

class MyClass914:
    def __init__(self, master):
        self.root = master
        self.root.resizable(width=False, height=False)
        self.root.title("Парсинг курса криптовалюты - Лежнев 914")
        self.root.geometry("400x400")

        self.lbl = Label(root, text="Курс Cardano")
        self.lbl.place(x=200, y=50, anchor="c")

        self.field = Entry()
        self.field.place(x=200, y=120, anchor="c")

        self.btn = Button(text="Показать", command=self.main)
        self.btn.place(x=200, y=180, anchor="c")

        menu = Menu(self.root)
        submenu = Menu(self.root)
        self.root.config(menu=menu)
        menu.add_cascade(label="Об авторе", menu=submenu, command=self.call_me)

    def call_me(self):
            self.messagebox.showinfo("Success", "Welcome to our tutorial")

    def get_html(self,url):
        # делаем запрос по адресу
        html_content = requests.get(url)
        # получаем содержание
        return html_content.text

    def get_data(self,html):
        soup = BeautifulSoup(html, 'lxml')
        t = soup.find('div', {'class': "priceValue"}) . find ('span')
        return t.text

    def main(self):
        url = 'https://coinmarketcap.com/ru/currencies/cardano/'
        res = self.get_html(url)
        print(self.get_data(res))
        self.field.delete(0, 'end')
        self.field.insert(0, self.get_data(res))

if __name__ == '__main__':
    root = Tk()
    win = MyClass914(root)
    root.mainloop()