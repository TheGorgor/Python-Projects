import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

SAVE_FILE = "students_data.txt"

class Student:
    def __init__(self, name):
        self.name = name
        self.payments = {}

    def add_year(self, year):
        if year not in self.payments:
            self.payments[year] = {month: "ödenmedi" for month in [
                "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
                "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]}

    def set_payment(self, year, month, status):
        self.add_year(year)
        if month in self.payments[year]:
            self.payments[year][month] = status

    def get_payment_status(self, year):
        return self.payments.get(year, {})

    def to_dict(self):
        return {"name": self.name, "payments": self.payments}

    @classmethod
    def from_dict(cls, data):
        student = cls(data["name"])
        student.payments = data["payments"]
        return student

class PaymentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bakırköy Satranç Merkezi Ödeme Takip")
        self.students = {}

        self.frame_left = tk.Frame(root)
        self.frame_left.pack(side=tk.LEFT, fill=tk.Y)

        self.frame_right = tk.Frame(root)
        self.frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.frame_left)
        self.listbox.pack(fill=tk.Y, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.display_payment_info)

        tk.Button(self.frame_left, text="Öğrenci Ekle", command=self.add_student).pack(fill=tk.X)
        tk.Button(self.frame_left, text="Öğrenci Sil", command=self.delete_student).pack(fill=tk.X)
        tk.Button(self.frame_left, text="Ödeme Durumu", command=self.check_payment).pack(fill=tk.X)
        tk.Button(self.frame_left, text="Ödeme Güncelle", command=self.update_payment).pack(fill=tk.X)
        tk.Button(self.frame_left, text="Verileri Dışa Aktar", command=self.export_data).pack(fill=tk.X)

        self.text_info = tk.Text(self.frame_right, state="disabled")
        self.text_info.pack(fill=tk.BOTH, expand=True)

        self.load_data()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_student(self):
        name = simpledialog.askstring("Öğrenci Adı", "Ad-Soyad girin:")
        if name:
            if name not in self.students:
                self.students[name] = Student(name)
                self.listbox.insert(tk.END, name)
                self.save_data()
            else:
                messagebox.showinfo("Uyarı", "Bu öğrenci zaten var.")

    def delete_student(self):
        selected = self.get_selected_student()
        if selected:
            confirm = messagebox.askyesno("Emin misin?", f"{selected} isimli öğrenci silinsin mi?")
            if confirm:
                del self.students[selected]
                self.refresh_listbox()
                self.save_data()
                self.text_info.config(state="normal")
                self.text_info.delete("1.0", tk.END)
                self.text_info.config(state="disabled")
                messagebox.showinfo("Silindi", f"{selected} başarıyla silindi.")

    def check_payment(self):
        selected = self.get_selected_student()
        if selected:
            year = simpledialog.askstring("Yıl", "Hangi yıl? (örn. 2025)")
            if year:
                status = self.students[selected].get_payment_status(year)
                if not status:
                    messagebox.showinfo("Bilgi", "Bu yıl için kayıt yok.")
                else:
                    result = f"{selected} - {year} Ödeme Durumu:\n"
                    for month, stat in status.items():
                        result += f"{month}: {stat}\n"
                    messagebox.showinfo("Durum", result)

    def update_payment(self):
        selected = self.get_selected_student()
        if selected:
            year = simpledialog.askstring("Yıl", "Yıl girin:")
            month = simpledialog.askstring("Ay", "Ay girin (örn. Ocak):")
            status = simpledialog.askstring("Durum", "Durum (ödendi/ödenmedi):")
            if year and month and status:
                self.students[selected].set_payment(year, month, status)
                self.save_data()
                self.display_payment_info()
                messagebox.showinfo("Başarılı", f"{month} {year} durumu güncellendi.")

    def get_selected_student(self):
        try:
            index = self.listbox.curselection()[0]
            return self.listbox.get(index)
        except IndexError:
            messagebox.showwarning("Hata", "Öğrenci seçilmedi.")
            return None

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for name in self.students:
            self.listbox.insert(tk.END, name)

    def save_data(self):
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump([student.to_dict() for student in self.students.values()], f, ensure_ascii=False, indent=4)

    def load_data(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    student = Student.from_dict(item)
                    self.students[student.name] = student
                    self.listbox.insert(tk.END, student.name)

    def export_data(self):
        with open("students_export.txt", "w", encoding="utf-8") as f:
            for student in self.students.values():
                f.write(f"{student.name}\n")
                for year, months in student.payments.items():
                    f.write(f"  {year}:\n")
                    for month, status in months.items():
                        f.write(f"    {month}: {status}\n")
                f.write("\n")

    def display_payment_info(self, event=None):
        selected = self.get_selected_student()
        if selected:
            self.text_info.config(state="normal")
            self.text_info.delete("1.0", tk.END)
            student = self.students[selected]
            for year, months in student.payments.items():
                self.text_info.insert(tk.END, f"{year}:\n")
                for month, status in months.items():
                    self.text_info.insert(tk.END, f"  {month}: {status}\n")
            self.text_info.config(state="disabled")

    def on_close(self):
        self.save_data()
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()
