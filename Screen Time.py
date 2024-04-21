#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv 

FILENAME = "Schmidt.csv"

class DataEntryForm(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()

        style = ttk.Style()
        style.theme_use("default")

        # Defines variables for text entry
        # User Info Section
        self.Fname = tk.StringVar()
        self.Lname = tk.StringVar()
        self.Age = tk.StringVar()  
        # Screen Time
        self.Favapp = tk.StringVar()
        self.Dtype = tk.StringVar()
        self.Hday = tk.StringVar()  
        # Mental Health
        self.Positive = tk.StringVar()    
        # Agree and Submit
        self.Agree = tk.StringVar()  


        # Dropdown Options - Screen Time
        Favorite_App = ["","Social Media Apps", "Game Apps", "Video Streaming Apps", "Other"]
        Device_Type = ["","Desktop", "Laptop", "Tablet", "Phone", "Other"]

        # Creates the frames for Entry Form
        User_Info = ttk.LabelFrame(self, text="User Info")
        User_Info.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        Screen_Time = ttk.LabelFrame(self, text="Screen Time")  
        Screen_Time.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

        Mental_Health = ttk.LabelFrame(self, text="Mental Health")
        Mental_Health.grid(column=0, row=2, padx=5, pady=5, sticky="nsew")

        Agree_Submit = ttk.LabelFrame(self, text="Agreement & Submission")
        Agree_Submit.grid(column=0, row=3, padx=5, pady=5, sticky="nsew")

        # Evenly distributes frame inside root geometry
        User_Info.columnconfigure(0, weight=1)
        Screen_Time.columnconfigure(0, weight=1)
        Mental_Health.columnconfigure(0, weight=1)
        Agree_Submit.columnconfigure(0, weight=1)


        # Labels and Text Entry for User Info
        ttk.Label(User_Info, text="First Name:").grid(
            column=0, row=0, sticky=tk.W)
        ttk.Entry(User_Info, width=25, textvariable=self.Fname).grid(
            column=0, row=1)

        ttk.Label(User_Info, text="Last Name:").grid(
            column=1, row=0, sticky=tk.W)
        ttk.Entry(User_Info, width=25, textvariable=self.Lname).grid(
            column=1, row=1)

        ttk.Label(User_Info, text="Age:").grid(
            column=2, row=0, sticky=tk.W)
        ttk.Spinbox(User_Info, width=23, from_=1, to=100, textvariable=self.Age).grid(
            column=2, row=1)

        # Labels and Text Entry for Screen Time
        ttk.Label(Screen_Time, text="Favorite App:").grid(
            column=0, row=0, sticky=tk.W)
        ttk.OptionMenu(Screen_Time, self.Favapp, *Favorite_App).grid(
            column=0, row=1, sticky=tk.W)

        ttk.Label(Screen_Time, text="Device Type:").grid(
            column=1, row=0, sticky=tk.W)
        ttk.OptionMenu(Screen_Time, self.Dtype, *Device_Type).grid(
            column=1, row=1, sticky=tk.W)

        ttk.Label(Screen_Time, text="AVG Hours/Day:").grid(
            column=2, row=0, sticky=tk.W)
        ttk.Spinbox(Screen_Time, width=23, from_=0, to=24, textvariable=self.Hday).grid(
            column=2, row=1, sticky=tk.W)
        
        # Labels and Text Entry for Mental Health
        ttk.Label(Mental_Health, text="Has your screen time positivley or negativley impacted your mental health?").grid(
            columnspan=2, row=0, sticky=tk.W)
        ttk.Radiobutton(Mental_Health, text="Positive", variable=self.Positive, value="Positive").grid(
            column=0, row=1)
        ttk.Radiobutton(Mental_Health, text="Negative", variable=self.Positive, value="Negative").grid(
            column=1, row=1)
        
        # Lables and Text Entry for Agreement & Submission
        ttk.Label(Agree_Submit, text="By proceeding, do you consent to the storage and utilization of your data \n for the purpose of a case study?").grid(
            columnspan=2, row=0, sticky=tk.W)
        ttk.Checkbutton(Agree_Submit, text="I agree", variable=self.Agree).grid(
            column=0, row=1, sticky=tk.E) 
        Agree_Submit.grid_rowconfigure(1, weight=1)   
        ttk.Button(Agree_Submit, text="Submit Data", command=self.check_data).grid(
            column=0, row=2)
        ttk.Button(Agree_Submit, text="See Entries", command=self.get_data).grid(
            column=1, row=2)
        
        # Evenly distributes widgets inside of frame
        User_Info.columnconfigure(0, weight=1)
        User_Info.columnconfigure(1, weight=1)
        User_Info.columnconfigure(2, weight=1)
        User_Info.columnconfigure(3, weight=1)

        Screen_Time.columnconfigure(0, weight=1)
        Screen_Time.columnconfigure(1, weight=1)

        Mental_Health.columnconfigure(0, weight=1)
        Mental_Health.columnconfigure(1, weight=1)

        Agree_Submit.columnconfigure(0, weight=1)
        Agree_Submit.columnconfigure(1, weight=1)

    #Checks to see if all fields are filled out.
    def check_data(self):
        if self.Fname.get() == "" or self.Lname.get() == "" or self.Age.get() == "" or self.Favapp.get() == "" or self.Dtype.get() == "" or self.Hday.get() == "" or self.Positive.get() == "":
                messagebox.showerror("Error", "Please fill out all fields")
                return
        #Checks to see if the user agreed to their info being sumbitted
        if not self.Agree.get():
            messagebox.showerror("Error", "Please agree to the data being submitted")
            return
        else:
            self.save_data()            
            
    #Writes to CSV FILE
    def save_data(self):
        # Determine the impact on mental health based on the selected radiobutton
        data = [
        self.Fname.get(),
        self.Lname.get(),
        self.Age.get(),
        self.Favapp.get(),
        self.Dtype.get(),
        self.Hday.get(),
        self.Positive.get()
        ]
        try:
            # Opens CSV file and appends data to it
            with open(FILENAME, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)

            messagebox.showinfo("Success", "Data submitted successfully")

            # Clears the entry boxes .set(methods)
            self.Fname.set("")
            self.Lname.set("")
            self.Age.set("")
            self.Favapp.set("")
            self.Dtype.set("")
            self.Hday.set("")
            self.Positive.set("") 
            self.Agree.set(False)

        except Exception as e:
            messagebox.showerror("Error", f"Data could not be submitted: {e}")

    # Reads from CSV and prints it to the terminal. Also saves entries to variable for second tkinter.
    def get_data(self):
        self.entries = []
        self.current_entry=0
        try:
            with open(FILENAME, mode='r', newline="") as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    self.entries.append(row)
                    print(','.join(row))  # Join the elements of each row with commas for display
                #if self.entries:
            self.display_entry(self)
        except Exception as f:
            print(f"Unable to open CSV file: {f}")
    
    #Another Tkinter window so users can see the data without modification
    def display_entry(self, entry):
        if self.entries:
            entry = self.entries[self.current_entry]
            window = tk.Toplevel(self)
            window.title("Data Entries")
            window.geometry("260x200")

            self.toplevel = window

            # Create a frame to contain all widgets
            main_frame = ttk.Frame(window)
            main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            ttk.Label(main_frame, text="First Name:").grid(row=0, column=0, sticky=tk.W)
            ttk.Label(main_frame, text=entry[0]).grid(row=0, column=1)

            ttk.Label(main_frame, text="Last Name:").grid(row=1, column=0, sticky=tk.W)
            ttk.Label(main_frame, text=entry[1]).grid(row=1, column=1)

            ttk.Label(main_frame, text="Age:").grid(row=2, column=0, sticky=tk.W)
            ttk.Label(main_frame, text=entry[2]).grid(row=2, column=1)

            ttk.Label(main_frame, text="Favorite App:").grid(row=3, column=0, sticky=tk.W)
            ttk.Label(main_frame, text=entry[3]).grid(row=3, column=1)

            ttk.Label(main_frame, text="Device Type:").grid(row=4, column=0, sticky=tk.W)
            ttk.Label(main_frame, text=entry[4]).grid(row=4, column=1)

            ttk.Label(main_frame, text="AVG Hours/Day:").grid(row=5, column=0, sticky=tk.W)
            ttk.Label(main_frame, text=entry[5]).grid(row=5, column=1)

            ttk.Label(main_frame, text="Mental Health Impact:").grid(row=6, column=0, sticky=tk.W)
            ttk.Label(main_frame, text=entry[6]).grid(row=6, column=1)

            # Create a frame to contain the buttons
            button_frame = ttk.Frame(main_frame)
            button_frame.grid(row=7, column=0, columnspan=2, pady=10)

            ttk.Button(button_frame, text="Back", command=self.load_previous).pack(side=tk.LEFT, padx=5)
            ttk.Button(button_frame, text="Close", command=window.destroy).pack(side=tk.LEFT, padx=5)
            ttk.Button(button_frame, text="Next", command=self.load_next).pack(side=tk.LEFT, padx=5)

        else:
            messagebox.showinfo("No entries", "There are no entries to display.")


    #Loads the next entry and destroys the previous
    def load_next(self):
        if self.current_entry < len(self.entries)-1:
            self.current_entry += 1
            if self.toplevel:
                self.toplevel.destroy()
            self.display_entry(self.entries[self.current_entry])
        else:
            messagebox.showinfo("No more entries", "There are no more entries")

    #Loads the previous entry and destroys the next
    def load_previous(self):
        if self.current_entry > 0:
            self.current_entry -= 1
            if self.toplevel:
                self.toplevel.destroy()
            self.display_entry(self.entries[self.current_entry])
        else:
            messagebox.showinfo("No previous entries", "You are already at the first entry")

   
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Data Entry Form - Schmidt")
    root.geometry("500x320")
    DataEntryForm(root)
    root.mainloop()
