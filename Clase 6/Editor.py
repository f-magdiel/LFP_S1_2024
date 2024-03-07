import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de texto")

        self.editor_frame = tk.Frame(root)
        self.editor_frame.pack(fill=tk.BOTH, expand=True)

        self.line_number_bar = tk.Text(self.editor_frame, width=4, padx=4, takefocus=0, border=0, background='lightgrey', state='disabled')
        self.line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

        self.text_widget = ScrolledText(self.editor_frame, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill='both')

        self.text_widget.bind('<Key>', self.update_line_numbers)
        self.text_widget.bind('<MouseWheel>', self.update_line_numbers)

        self.current_line = 1

        self.second_editor_frame = tk.Frame(root)
        self.second_editor_frame.pack(fill=tk.BOTH, expand=True)

        self.second_line_number_bar = tk.Text(self.second_editor_frame, width=4, padx=4, takefocus=0, border=0, background='lightgrey', state='disabled')
        self.second_line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

        self.second_text_widget = ScrolledText(self.second_editor_frame, wrap=tk.WORD, state='disabled')
        self.second_text_widget.pack(expand=True, fill='both')

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)

        # Nuevo botón para mostrar el texto cargado
        self.show_button = tk.Button(root, text="Mostrar Texto", command=self.show_text)
        self.show_button.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
            self.update_line_numbers()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt")])
        if file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")

    def update_line_numbers(self, event=None):
        line_count = self.text_widget.get('1.0', tk.END).count('\n')
        if line_count != self.current_line:
            self.line_number_bar.config(state=tk.NORMAL)
            self.line_number_bar.delete(1.0, tk.END)
            for line in range(1, line_count + 1):
                self.line_number_bar.insert(tk.END, f"{line}\n")
            self.line_number_bar.config(state=tk.DISABLED)
            self.current_line = line_count

    def show_text(self):
        text = self.text_widget.get(1.0, tk.END)
        self.second_text_widget.config(state='normal')
        self.second_text_widget.delete(1.0, tk.END)
        self.second_text_widget.insert(tk.END, text)
        self.second_text_widget.tag_configure("green", foreground="green")
        self.second_text_widget.tag_add("green", "1.0", "end")
        self.second_text_widget.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

