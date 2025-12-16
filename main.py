import tkinter as tk
from tkinter import Label, Button, Toplevel
from PIL import Image, ImageTk
from student1 import Student
import os
from train import Train
from face_recognition import FaceRecognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        try:
            img_path1 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\Projectupperimage2.jpg"
            img1 = Image.open(img_path1)
            img1 = img1.resize((500, 130), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_lbl1 = Label(self.root, image=self.photoimg1)
            f_lbl1.place(x=0, y=0, width=500, height=130)
        except Exception as e:
            print(f"Error loading image 1: {e}")

        # Second Image
        try:
            img_path2 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\Projectupperimage5.jpg"
            img2 = Image.open(img_path2)
            img2 = img2.resize((500, 130), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=500, y=0, width=500, height=130)
        except Exception as e:
            print(f"Error loading image 2: {e}")

        # Third Image
        try:
            img_path3 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\Projectupperimage6.jpg"
            img3 = Image.open(img_path3)
            img3 = img3.resize((500, 130), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            f_lbl3 = Label(self.root, image=self.photoimg3)
            f_lbl3.place(x=1000, y=0, width=530, height=130)
        except Exception as e:
            print(f"Error loading image 3: {e}")

        # Background Image
        try:
            img_path4 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\backgroundimage.jpg"
            img4 = Image.open(img_path4)
            img4 = img4.resize((1530, 710), Image.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            bg_img = Label(self.root, image=self.photoimg4)
            bg_img.place(x=0, y=130, width=1530, height=710)
        except Exception as e:
            print(f"Error loading background image: {e}")

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student Button
        try:
            img_path5 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\studentsimg.webp"
            img5 = Image.open(img_path5)
            img5 = img5.resize((220, 220), Image.LANCZOS)
            self.photoimg5 = ImageTk.PhotoImage(img5)

            b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
            b1.place(x=200, y=100, width=220, height=220)

            b1_text = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b1_text.place(x=200, y=300, width=220, height=40)

        except Exception as e:
            print(f"Error loading student button image: {e}")

       # Detect face button
        try:
            img_path6 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\trainphoto.webp"
            img6 = Image.open(img_path6)
            img6 = img6.resize((220, 220), Image.LANCZOS)
            self.photoimg6 = ImageTk.PhotoImage(img6)

            b2 = Button(bg_img, command=self.face_data, image=self.photoimg6, cursor="hand2")  # Corrected 'command'
            b2.place(x=500, y=100, width=220, height=220)

            b2_text = Button(bg_img, command=self.face_data, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b2_text.place(x=500, y=300, width=220, height=40)

        except Exception as e:
            print(f"Error loading face detector button image: {e}")


        # Attendance button
        try:
            img_path7 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\Attendance2.jpg"
            img7 = Image.open(img_path7)
            img7 = img7.resize((220, 220), Image.LANCZOS)
            self.photoimg7 = ImageTk.PhotoImage(img7)

            b3 = Button(bg_img, image=self.photoimg7, cursor="hand2")
            b3.place(x=800, y=100, width=220, height=220)

            b3_text = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b3_text.place(x=800, y=300, width=220, height=40)

        except Exception as e:
            print(f"Error loading attendance button image: {e}")

        # Help desk button
        try:
            img_path8 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\help-desk.webp"
            img8 = Image.open(img_path8)
            img8 = img8.resize((220, 220), Image.LANCZOS) 
            self.photoimg8 = ImageTk.PhotoImage(img8)

            b4 = Button(bg_img, image=self.photoimg8, cursor="hand2")
            b4.place(x=1100, y=100, width=220, height=220)

            b4_text = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b4_text.place(x=1100, y=300, width=220, height=40)

        except Exception as e:
            print(f"Error loading help desk button image: {e}")

        # Train Face button
        try:
            img_path9 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\Train.jpg"
            img9 = Image.open(img_path9)
            img9 = img9.resize((220, 220), Image.LANCZOS)
            self.photoimg9 = ImageTk.PhotoImage(img9)

            b5 = Button(bg_img, image=self.photoimg9, command=self.train_data, cursor="hand2")
            b5.place(x=200, y=380, width=220, height=220)

            b5_text = Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b5_text.place(x=200, y=580, width=220, height=40)

        except Exception as e:
            print(f"Error loading train data button image: {e}")

        # Photo button
        try:
            img_path10 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\Photos.jpg"
            img10 = Image.open(img_path10)
            img10 = img10.resize((220, 220), Image.LANCZOS)
            self.photoimg10 = ImageTk.PhotoImage(img10)

            b6 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_img)
            b6.place(x=500, y=380, width=220, height=220)

            b6_text = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b6_text.place(x=500, y=580, width=220, height=40)

        except Exception as e:
            print(f"Error loading photos button image: {e}")

        # Developer button
        try:
            img_path11 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\Developer.png"
            img11 = Image.open(img_path11)
            img11 = img11.resize((220, 220), Image.LANCZOS)
            self.photoimg11 = ImageTk.PhotoImage(img11)

            b7 = Button(bg_img, image=self.photoimg11, cursor="hand2")
            b7.place(x=800, y=380, width=220, height=220)

            b7_text = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b7_text.place(x=800, y=580, width=220, height=40)

        except Exception as e:
            print(f"Error loading developer button image: {e}")

        # Exit button
        try:
            img_path12 = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\Exit.jpg"
            img12 = Image.open(img_path12)
            img12 = img12.resize((220, 220), Image.LANCZOS)
            self.photoimg12 = ImageTk.PhotoImage(img12)

            b8 = Button(bg_img, image=self.photoimg12, cursor="hand2", command=self.root.quit)
            b8.place(x=1100, y=380, width=220, height=220)

            b8_text = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", command=self.root.quit)
            b8_text.place(x=1100, y=580, width=220, height=40)

        except Exception as e:
            print(f"Error loading exit button image: {e}")

    def open_img(self):
        os.startfile("data")

    # ==== Function Buttons =====#
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)











if __name__ == "__main__":      
    root = tk.Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
