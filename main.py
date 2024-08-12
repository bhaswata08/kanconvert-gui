import tkinter as tk
from tkinter import filedialog, messagebox
from src.docx_processor import convert_docx  # Import the convert_docx function from your original script

class KannadaConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Kannada ASCII to Unicode Converter')
        self.master.geometry('400x200')
        
        self.input_file = None
        
        self.create_widgets()
        
    def create_widgets(self):
        # Select File Button
        self.select_file_button = tk.Button(self.master, text='Select File', command=self.select_file)
        self.select_file_button.pack(pady=10)
        
        # File Label
        self.file_label = tk.Label(self.master, text='No file selected')
        self.file_label.pack(pady=5)
        
        # Process File Button
        self.process_button = tk.Button(self.master, text='Process File', command=self.process_file, state=tk.DISABLED)
        self.process_button.pack(pady=10)
        
    def select_file(self):
        self.input_file = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
        if self.input_file:
            self.file_label.config(text=f"Selected file: {self.input_file}")
            self.process_button.config(text=f"Process file: {self.input_file.split('/')[-1]}", state=tk.NORMAL)
        
    def process_file(self):
        if not self.input_file:
            return
        
        output_file = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])
        
        if output_file:
            try:
                convert_docx(self.input_file, output_file)
                messagebox.showinfo("Success", f"File successfully processed and saved at: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while processing the file: {str(e)}")

def main():
    root = tk.Tk()
    app = KannadaConverterGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()