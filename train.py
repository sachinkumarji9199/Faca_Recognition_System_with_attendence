import tkinter as tk
from tkinter import messagebox, Button
from PIL import Image, ImageTk
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = tk.Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #  the top image
        img_top_path = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\Projectupperimage5.jpg"
        if os.path.exists(img_top_path):
            img_top = Image.open(img_top_path)
            img_top = img_top.resize((1530, 325), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            f_lbl_top = tk.Label(self.root, image=self.photoimg_top)
            f_lbl_top.place(x=0, y=45, width=1530, height=325)
        else:
            print(f"Error: Image path '{img_top_path}' does not exist")

        # Buttons
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        #  the bottom image
        img_bottom_path = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\trainphoto2.webp"
        if os.path.exists(img_bottom_path):
            img_bottom = Image.open(img_bottom_path)
            img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

            f_lbl_bottom = tk.Label(self.root, image=self.photoimg_bottom)
            f_lbl_bottom.place(x=0, y=450, width=1530, height=325)
        else:
            print(f"Error: Image path '{img_bottom_path}' does not exist")

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image_path in path:
            img = Image.open(image_path).convert('L')  # Convert color image to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image_path)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # ========== Train the classifier and save ======== #
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")

if __name__ == "__main__":
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()
