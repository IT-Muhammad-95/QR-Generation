import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import ImageTk


def generate_qr_image(url):
    """Генерирует QR-код и возвращает объект PIL Image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def show_qr_window(url):
    """Открывает окно tkinter с предпросмотром QR-кода и кнопкой сохранения."""
    # Генерируем изображение
    qr_image = generate_qr_image(url)

    # Создаём окно
    window = tk.Tk()
    window.title("QR-код")
    window.resizable(False, False)

    # Конвертируем PIL Image в формат, понятный tkinter
    qr_tk_image = ImageTk.PhotoImage(qr_image)

    # Метка с изображением
    label = tk.Label(window, image=qr_tk_image)
    label.image = qr_tk_image  # сохраняем ссылку, чтобы не удалилось сборщиком мусора
    label.pack(padx=20, pady=20)

    # Функция сохранения
    def save_qr():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            initialfile="qrcode.png",
            title="Сохранить QR-код"
        )
        if file_path:
            qr_image.save(file_path)
            messagebox.showinfo("Успех", f"QR-код сохранён:\n{file_path}")

    # Функция закрытия
    def close_window():
        window.destroy()

    # Кнопки
    btn_save = tk.Button(window, text="Сохранить", command=save_qr, width=15)
    btn_save.pack(side=tk.LEFT, padx=10, pady=10)

    btn_close = tk.Button(window, text="Закрыть", command=close_window, width=15)
    btn_close.pack(side=tk.RIGHT, padx=10, pady=10)

    window.mainloop()


def main():
    """Терминальное меню с двумя пунктами."""
    while True:
        print("\n=== Генератор QR-кодов ===")
        print("1. Создать QR-код")
        print("2. Завершить программу")

        choice = input("Ваш выбор: ").strip()

        if choice == '1':
            url = input("Введите ссылку или текст: ").strip()
            if not url:
                print("❌ Пустой ввод. Попробуйте снова.")
                continue
            show_qr_window(url)
        elif choice == '2' or choice == 'exit':
            print("Программа завершена.")
            break
        else:
            print("❌ Неверный выбор. Введите 1 или 2.")


if __name__ == '__main__':
    main()