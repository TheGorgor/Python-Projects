class Student:
    def __init__(self, first_name, last_name, student_id, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.grade = grade

    def __str__(self):
        return (f"Ad - Soyad: {self.first_name} {self.last_name}\n"
                f"Numara: {self.student_id}\n"
                f"Sınıf: {self.grade}")

students = []

def add_student():
    print("Yeni öğrenci ekle \n")
    first_name = input("Öğrencinin adı: ")
    last_name = input("Öğrencinin soyadı: ")
    student_id = input("Öğrencinin numarası: ")  # Bu kısmı string olarak alıyoruz
    grade = input("Öğrencinin sınıfı:")

    student = Student(first_name, last_name, student_id, grade)
    students.append(student)

    print("Öğrenci başarıyla eklendi!")

def display_students():
    print("Kayıtlı öğrenciler")
    print("==================")
    if not students:
        print("Kayıtlı öğrenci bulunamadı.")
        return
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student}")

def delete_student():
    print("Öğrenciyi sil")
    try:
        student_id = input("Silmek istediğiniz öğrencinin numarasını girin: ").strip()  # ID'yi string olarak alıyoruz

        # Silinecek öğrenciyi bulalım
        student = next((stu for stu in students if stu.student_id.strip() == student_id), None)

        if student:
            students.remove(student)
            print(f"{student.first_name} {student.last_name} başarıyla silindi.")
        else:
            print("Öğrenci bulunamadı.")

    except ValueError:
        print("Geçerli bir numara girin.")

def export():
    print("Dışa aktarma")
    try:
        with open("C:/Users/Victus/Desktop/Öğrenciler/öğrenciler.txt", "w") as file:
            for student in students:
                file.write(f"{student.first_name} {student.last_name} - {student.student_id} - {student.grade}. Sınıf \n")
        print("Veri başarıyla dışa aktarıldı. Verilere \"Öğrenciler\" dosyasında erişebilirsiniz.")
    except Exception as e:
        print(f"Veriler dışa aktarılırken bir sıkıntı oluştu\n {e}")

def main_menu():
    while True:
        print("Öğrenci kayıt sistemi")
        print("1. Öğrenci Ekle")
        print("2. Öğrencileri Listele")
        print("3. Öğrenci Sil")
        print("4. Dışa Aktar")
        print("5. Çıkış")

        main_menu_choice = int(input("Bir seçenek girin (1-5): "))

        if main_menu_choice == 1:
            add_student()
        elif main_menu_choice == 2:
            display_students()
        elif main_menu_choice == 3:
            delete_student()
        elif main_menu_choice == 4:
            export()
        elif main_menu_choice == 5:
            print("Çıkılıyor... Görüşürüz")
            break
        else:
            print("Geçersiz seçim, lütfen 1-5 arasında bir seçenek girin.")

main_menu()
