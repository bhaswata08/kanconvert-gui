import tkinter as tk
from tkinter import filedialog, messagebox
from src.kanconverter import process_line
from src.file_reader import read_file
from src.file_writer import write_file  # You'll need to create this module

class TextProcessorApp:
    def __init__(self, master):
        self.master = master
        master.title("Text Processor")
        master.geometry("500x300")

        # Input text area
        self.input_label = tk.Label(master, text="Input Text:")
        self.input_label.pack()
        self.input_text = tk.Text(master, height=10)
        self.input_text.pack()

        # Process and Save button
        self.process_button = tk.Button(master, text="Process and Save", command=self.process_and_save)
        self.process_button.pack()

        # File selection button
        self.file_button = tk.Button(master, text="Select File", command=self.select_file)
        self.file_button.pack()

    def process_and_save(self):
        input_txt = self.input_text.get("1.0", tk.END).strip()
        if input_txt:
            processed_text = process_line(input_txt)
            self.save_file(processed_text)
        else:
            messagebox.showwarning("Warning", "Please enter some text to process.")

    def save_file(self, content):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("Word files", "*.docx")]
        )
        if file_path:
            try:
                write_file(file_path, content)  # Use the write_file function
                messagebox.showinfo("Success", f"File saved successfully: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf"), ("Word files", "*.docx")])
        if file_path:
            try:
                content = read_file(file_path)  # Use the read_file function
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process file: {str(e)}")

def main():
    root = tk.Tk()
    app = TextProcessorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
