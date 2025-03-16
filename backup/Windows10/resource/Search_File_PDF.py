import tkinter as tk
from tkinter import filedialog
import os
import datetime as dt
import PyPDF2

selected_files = []

def search_files():
    global selected_files
    selected_files.clear()
    keyword = keyword_entry.get()
    search_type = search_type_var.get()
    time_filter = time_filter_var.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    selected_path = path_entry.get()

    if not keyword or not selected_path:
        result_listbox.delete(0, tk.END)
        result_listbox.insert(tk.END, "Please fill in all the required fields.")
        return

    if time_filter == "Searching Start From" or time_filter == "Searching Start and End From":
        try:
            start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            result_listbox.delete(0, tk.END)
            result_listbox.insert(tk.END, "Invalid start date format. Use YYYY-MM-DD.")
            return

    if time_filter == "Searching End From" or time_filter == "Searching Start and End From":
        try:
            end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            result_listbox.delete(0, tk.END)
            result_listbox.insert(tk.END, "Invalid end date format. Use YYYY-MM-DD.")
            return

    result_listbox.delete(0, tk.END)
    for root, _, files in os.walk(selected_path):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                mod_time = dt.datetime.fromtimestamp(os.path.getmtime(file_path))

                if time_filter == "Searching Start From" and mod_time.date() < start_date.date():
                    continue
                if time_filter == "Searching End From" and mod_time.date() > end_date.date():
                    continue
                if time_filter == "Searching Start and End From" and (mod_time.date() < start_date.date() or mod_time.date() > end_date.date()):
                    continue

                if search_type == "File Name Search" and keyword.lower() in file.lower():
                    result_listbox.insert(tk.END, file)
                elif search_type == "File Content Search":
                    try:
                        with open(file_path, 'rb') as pdf_file:
                            pdf_reader = PyPDF2.PdfReader(pdf_file)
                            for page_num in range(len(pdf_reader.pages)):
                                page = pdf_reader.pages[page_num]
                                if keyword.lower() in page.extract_text().lower():
                                    result_listbox.insert(tk.END, file)
                                    break
                    except:
                        continue

def browse_path():
    path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, path)

def open_selected_files():
    selected_indices = result_listbox.curselection()
    for index in selected_indices:
        file_name = result_listbox.get(index)
        for root, _, files in os.walk(path_entry.get()):
            for file in files:
                if file == file_name:
                    file_path = os.path.join(root, file)
                    os.startfile(file_path)

root = tk.Tk()
root.title("Search File (PDF)")

# Set minimum size of the window
root.minsize(400, 400)

# Create a Frame for the resizable part
resizable_frame = tk.Frame(root)
resizable_frame.pack(fill=tk.BOTH, expand=True)

root.geometry("600x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

search_type_var = tk.StringVar()
search_type_var.set("File Name Search")

search_type_frame = tk.Frame(resizable_frame)
search_type_frame.pack()

search_type_label = tk.Label(search_type_frame, text="Search Type:")
search_type_label.pack(side=tk.LEFT)

search_type_radio_file = tk.Radiobutton(search_type_frame, text="File Name Search", variable=search_type_var, value="File Name Search")
search_type_radio_file.pack(side=tk.LEFT)

search_type_radio_content = tk.Radiobutton(search_type_frame, text="File Content Search", variable=search_type_var, value="File Content Search")
search_type_radio_content.pack(side=tk.LEFT)

keyword_label = tk.Label(resizable_frame, text="Enter Keyword:")
keyword_label.pack()

keyword_entry = tk.Entry(resizable_frame)
keyword_entry.pack()

time_filter_var = tk.StringVar()
time_filter_var.set("All Time")

time_filter_frame = tk.Frame(resizable_frame)
time_filter_frame.pack()

time_filter_label = tk.Label(time_filter_frame, text="Time Filter:")
time_filter_label.pack(side=tk.LEFT)

time_filter_radio_all = tk.Radiobutton(time_filter_frame, text="All Time", variable=time_filter_var, value="All Time")
time_filter_radio_all.pack(side=tk.LEFT)

time_filter_radio_start = tk.Radiobutton(time_filter_frame, text="Searching Start From", variable=time_filter_var, value="Searching Start From")
time_filter_radio_start.pack(side=tk.LEFT)

time_filter_radio_end = tk.Radiobutton(time_filter_frame, text="Searching End From", variable=time_filter_var, value="Searching End From")
time_filter_radio_end.pack(side=tk.LEFT)

time_filter_radio_both = tk.Radiobutton(time_filter_frame, text="Searching Start and End From", variable=time_filter_var, value="Searching Start and End From")
time_filter_radio_both.pack(side=tk.LEFT)

start_date_label = tk.Label(resizable_frame, text="Enter Start Date (YYYY-MM-DD):")
start_date_label.pack()

start_date_entry = tk.Entry(resizable_frame)
start_date_entry.pack()

end_date_label = tk.Label(resizable_frame, text="Enter End Date (YYYY-MM-DD):")
end_date_label.pack()

end_date_entry = tk.Entry(resizable_frame)
end_date_entry.pack()

path_label = tk.Label(resizable_frame, text="Select Path:")
path_label.pack()

path_entry = tk.Entry(resizable_frame)
path_entry.pack()

browse_button = tk.Button(resizable_frame, text="Browse", command=browse_path)
browse_button.pack(pady=10)

search_button = tk.Button(resizable_frame, text="Search Files", command=search_files)
search_button.pack()

open_files_button = tk.Button(resizable_frame, text="Open Selected Files", command=open_selected_files)
open_files_button.pack(pady=10)

result_listbox = tk.Listbox(resizable_frame, selectmode=tk.MULTIPLE, width=60)
result_listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()
