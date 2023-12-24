import tkinter as tk
from tkinter import messagebox
class RegistrationWindow:
    def __init__(self, filename):
        self.filename = filename
        self.acces = False
        self.window = tk.Tk()
        self.window.resizable(width=False,height=False)
        self.window['bg'] = "gray10"
        self.window.geometry('500x200')
        self.window.title("Регистрация")


        self.username_label = tk.Label(self.window, text="Логин:",bg="gray10", fg="gray99")
        self.username_label.place(relx = 0.45,rely = 0.02)


        self.username_entry = tk.Entry(self.window,bg='#fff', fg='#444')
        self.username_entry.place(width = 166, relx = 0.33, rely = 0.15)

        self.password_label = tk.Label(self.window, text="Пароль:", bg="gray10",fg="gray99")
        self.password_label.place(relx = 0.45, rely = 0.28)

        self.password_entry = tk.Entry(self.window, show="*",bg='#fff', fg='#444')
        self.password_entry.place(width = 166, relx = 0.33, rely = 0.4)

        self.register_button = tk.Button(self.window, text="Зарегистрироваться/Войти", command=self.register, bg="gray14",fg = "gray99")
        self.register_button.place(width = 200, relx = 0.3, rely = 0.6)

    def shifr(self, message1):
        alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        smeshenie = 4
        itog = ''
        message = message1.upper()
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
        print(itog)
        return itog
    def register(self):
        username = self.username_entry.get()
        password1 = self.password_entry.get()
        password = self.shifr(password1)

        if not username or not password:
            messagebox.showerror("Ошибка", "Введите логин и пароль")
            return

        # Проверяем, есть ли логин и пароль в файле
        with open(self.filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                saved_username, saved_password = line.strip().split(",")
                if username == saved_username and password == saved_password:
                    messagebox.showinfo("Успех", "Авторизация прошла успешно")
                    self.window.destroy()
                    self.acces = True
                    return
                elif username.upper().replace(' ','') == "ВАСЯПУПКИН":
                    for i in range(5):
                        messagebox.showinfo("Предупреждение", f"Вы{' точно '*i} уверены что хотите это имя пользователя")
                    messagebox.showinfo("Ошибка", "Пользователь с таким логином является администратором")

                    return
                elif username == saved_username:
                    messagebox.showinfo("Ошибка", "Пользователь с таким логином уже существует")

                    return
        with open(self.filename, "a") as f:
            f.write(f"{username},{password}\n")
            messagebox.showinfo("Успех", "Добро пожаловать\nРегистрация прошла успешно")
            self.window.destroy()
            self.acces = True
            return

    def run(self):
        self.window.mainloop()
    def accesf(self):
        b = self.acces
        return b








