import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, first_name, last_name, student_id, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.grade = grade

    def __str__(self):
        return f"Ad - Soyad: {self.first_name} {self.last_name}\nNumara: {self.student_id}\nSınıf: {self.grade}"

students = []

def add_student():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    student_id = student_id_entry.get()
    grade = grade_entry.get()  # Burada grade_entry kullanılıyor

    if first_name and last_name and student_id and grade:
        student = Student(first_name, last_name, student_id, grade)
        students.append(student)
        messagebox.showinfo("Başarılı", "Öğrenci başarıyla eklendi!")
        clear_entries()
        display_students()  # Yeni öğrenci ekledikten sonra listeyi güncelle
    else:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")

def display_students():
    students_listbox.delete(0, tk.END)  # Mevcut listeyi temizle
    if students:
        for student in students:
            students_listbox.insert(tk.END, str(student))
    else:
        messagebox.showinfo("Kayıt Yok", "Henüz kayıtlı öğrenci yok.")

def delete_student():
    student_id = delete_student_id_entry.get()

    if student_id:
        student = next((stu for stu in students if stu.student_id == student_id), None)
        if student:
            students.remove(student)
            messagebox.showinfo("Başarılı", f"{student.first_name} {student.last_name} başarıyla silindi!")
            delete_student_id_entry.delete(0, tk.END)  # Silinen ID'yi temizle
            display_students()  # Listeyi güncelle
        else:
            messagebox.showwarning("Bulunamadı", "Öğrenci bulunamadı.")
    else:
        messagebox.showwarning("Eksik ID", "Lütfen silmek istediğiniz öğrencinin ID'sini girin.")

def export_students():
    try:
        # Dosya yolunu belirliyoruz
        with open("C:/Users/Victus/Desktop/Öğrenciler/Öğrenciler.txt", "w") as file:
            # Öğrencileri dosyaya yazıyoruz
            for student in students:
                file.write(f"{student.first_name} {student.last_name} - {student.student_id} - {student.grade}.\n")
        messagebox.showinfo("Başarılı", "Veri başarıyla dışa aktarıldı! Dosyaya \"Öğrenciler\" adlı klasörden ulaşabilirsiniz.")
    except Exception as e:
        messagebox.showerror("Hata", f"Veri dışa aktarılırken bir hata oluştu: {e}")

def clear_entries():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    student_id_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)  # Burada da grade_entry'yi temizliyoruz

# GUI Penceresi
root = tk.Tk()
root.title("Öğrenci Kayıt Sistemi")

# Öğrenci Ekleme Bölümü
add_student_frame = tk.Frame(root)
add_student_frame.pack(pady=10)

tk.Label(add_student_frame, text="Ad: ").grid(row=0, column=0, padx=5, pady=5)
first_name_entry = tk.Entry(add_student_frame)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(add_student_frame, text="Soyad: ").grid(row=1, column=0, padx=5, pady=5)
last_name_entry = tk.Entry(add_student_frame)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(add_student_frame, text="Numara: ").grid(row=2, column=0, padx=5, pady=5)
student_id_entry = tk.Entry(add_student_frame)
student_id_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(add_student_frame, text="Sınıf: ").grid(row=3, column=0, padx=5, pady=5)
grade_entry = tk.Entry(add_student_frame)  # Burada grade_entry'yi tanımlıyoruz
grade_entry.grid(row=3, column=1, padx=5, pady=5)

add_student_button = tk.Button(add_student_frame, text="Öğrenci Ekle", command=add_student)
add_student_button.grid(row=4, columnspan=2, pady=10)

# Öğrenci Listeleme Bölümü
list_students_frame = tk.Frame(root)
list_students_frame.pack(pady=10)

students_listbox = tk.Listbox(list_students_frame, width=50, height=10)
students_listbox.pack(pady=10)

list_students_button = tk.Button(list_students_frame, text="Öğrencileri Listele", command=display_students)
list_students_button.pack()

# Öğrenci Silme Bölümü
delete_student_frame = tk.Frame(root)
delete_student_frame.pack(pady=10)

tk.Label(delete_student_frame, text="Silmek istediğiniz öğrencinin numarasını girin: ").pack(pady=5)
delete_student_id_entry = tk.Entry(delete_student_frame)
delete_student_id_entry.pack(pady=5)

delete_student_button = tk.Button(delete_student_frame, text="Öğrenci Sil", command=delete_student)
delete_student_button.pack(pady=10)

# Dışa Aktarma Bölümü
export_frame = tk.Frame(root)
export_frame.pack(pady=10)

export_button = tk.Button(export_frame, text="Öğrencileri Dışa Aktar", command=export_students)
export_button.pack(pady=10)

# Uygulamayı başlat
root.mainloop()
