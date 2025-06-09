#!/usr/bin/env python3
"""
Simple Tkinter GUI for WordcloudSR.
"""
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from threading import Thread

from wordcloudsr import process_files


class WordcloudGUI:
    """Simple Tkinter interface for WordcloudSR."""

    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        master.title("WordcloudSR GUI")

        # Input directory
        tk.Label(master, text="Input Directory:").grid(row=0, column=0, sticky="w")
        self.input_var = tk.StringVar(value="input")
        tk.Entry(master, textvariable=self.input_var, width=40).grid(row=0, column=1, padx=5)
        tk.Button(master, text="Browse", command=self.browse_input).grid(row=0, column=2)

        # Output directory
        tk.Label(master, text="Output Directory:").grid(row=1, column=0, sticky="w")
        self.output_var = tk.StringVar(value="output")
        tk.Entry(master, textvariable=self.output_var, width=40).grid(row=1, column=1, padx=5)
        tk.Button(master, text="Browse", command=self.browse_output).grid(row=1, column=2)

        # Stopwords file
        tk.Label(master, text="Stopwords File:").grid(row=2, column=0, sticky="w")
        self.stopwords_var = tk.StringVar(value="stopwords.txt")
        tk.Entry(master, textvariable=self.stopwords_var, width=40).grid(row=2, column=1, padx=5)
        tk.Button(master, text="Browse", command=self.browse_stopwords).grid(row=2, column=2)

        # Collocations checkbox
        self.collocations_var = tk.BooleanVar(value=True)
        tk.Checkbutton(master, text="Include Collocations", variable=self.collocations_var).grid(row=3, columnspan=3, pady=(5, 5), sticky="w")

        # Run button
        tk.Button(master, text="Process Files", command=self.run_process).grid(row=4, columnspan=3, pady=(5, 5))

        # Status area
        self.status = scrolledtext.ScrolledText(master, width=60, height=10, state="disabled")
        self.status.grid(row=5, columnspan=3, pady=(5, 0))

    def browse_input(self) -> None:
        directory = filedialog.askdirectory()
        if directory:
            self.input_var.set(directory)

    def browse_output(self) -> None:
        directory = filedialog.askdirectory()
        if directory:
            self.output_var.set(directory)

    def browse_stopwords(self) -> None:
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.stopwords_var.set(file_path)

    def run_process(self) -> None:
        Thread(target=self._process).start()

    def _process(self) -> None:
        self.append_status("Processing started...\n")
        try:
            results = process_files(
                collocations=self.collocations_var.get(),
                input_dir=self.input_var.get(),
                output_dir=self.output_var.get(),
                stopwords_file=self.stopwords_var.get(),
            )
            if results:
                self.append_status(f"Completed. Processed {len(results)} directories.\n")
            else:
                self.append_status("No results generated.\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.append_status(f"Error: {e}\n")

    def append_status(self, text: str) -> None:
        self.status.configure(state="normal")
        self.status.insert(tk.END, text)
        self.status.see(tk.END)
        self.status.configure(state="disabled")


def main() -> None:
    root = tk.Tk()
    app = WordcloudGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

