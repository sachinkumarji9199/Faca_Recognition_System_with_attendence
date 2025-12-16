import tkinter as tk
from tkinter import messagebox, Button
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = tk.Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_left_path = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\facephoto1.jpg"
        if os.path.exists(img_left_path):
            img_left = Image.open(img_left_path)
            img_left = img_left.resize((650, 700), Image.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            f_lbl_top = tk.Label(self.root, image=self.photoimg_left)
            f_lbl_top.place(x=0, y=55, width=650, height=700)
        else:
            messagebox.showerror("Error", f"Image path '{img_left_path}' does not exist")  # GUI feedback

        img_right_path = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\facephoto2.webp"
        if os.path.exists(img_right_path):
            img_right = Image.open(img_right_path)
            img_right = img_right.resize((870, 700), Image.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)
            f_lbl_right = tk.Label(self.root, image=self.photoimg_right)
            f_lbl_right.place(x=650, y=55, width=870, height=700)
        else:
            messagebox.showerror("Error", f"Image path '{img_right_path}' does not exist")  # GUI feedback

        b1_1 = Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="red", fg="white")
        b1_1.place(x=960, y=675, width=250, height=35)

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100 * (1 - predict/300)))

                # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="Sachin@123", database="face_recognizer")
                my_cursor = conn.cursor()

                # Fetch data from the database
                my_cursor.execute("select Name from student where Std_id=" + str(id))  # Potential SQL injection risk
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"  # Handle case when no result is fetched

                my_cursor.execute("select Roll from student where Std_id=" + str(id))  # Potential SQL injection risk
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"  # Handle case when no result is fetched
                
                my_cursor.execute("select Dep from student where Std_id=" + str(id))  # Potential SQL injection risk
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"  # Handle case when no result is fetched

                if confidence > 50:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # clf = cv2.face.LBPHFaceRecognizer_create()
        # clf.read("classifier.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:  # Handle case when frame is not captured
                print("Failed to capture video frame")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' key to exit
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    obj = FaceRecognition(root)
    root.mainloop()

# import tkinter as tk
# from tkinter import messagebox, Button
# from PIL import Image, ImageTk
# import mysql.connector
# import cv2
# import os

# class FaceRecognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         # Title
#         title_lbl = tk.Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         # Left image
#         img_left_path = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\facephoto1.jpg"
#         if os.path.exists(img_left_path):
#             img_left = Image.open(img_left_path).resize((650, 700), Image.LANCZOS)
#             self.photoimg_left = ImageTk.PhotoImage(img_left)
#             f_lbl_top = tk.Label(self.root, image=self.photoimg_left)
#             f_lbl_top.place(x=0, y=55, width=650, height=700)
#         else:
#             messagebox.showerror("Error", f"Image path '{img_left_path}' does not exist")

#         # Right image
#         img_right_path = r"C:\Users\princ\OneDrive\Desktop\Frontend Developer\Face-recongnition_system\facephoto2.webp"
#         if os.path.exists(img_right_path):
#             img_right = Image.open(img_right_path).resize((870, 700), Image.LANCZOS)
#             self.photoimg_right = ImageTk.PhotoImage(img_right)
#             f_lbl_right = tk.Label(self.root, image=self.photoimg_right)
#             f_lbl_right.place(x=650, y=55, width=870, height=700)
#         else:
#             messagebox.showerror("Error", f"Image path '{img_right_path}' does not exist")

#         # Button
#         b1_1 = Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2",
#                       font=("times new roman", 18, "bold"), bg="red", fg="white")
#         b1_1.place(x=960, y=675, width=250, height=35)

#     def face_recog(self):
#         def fetch_student_data():
#             """Fetch student data from the database and map IDs to details."""
#             conn = mysql.connector.connect(host="localhost", username="root", password="Sachin@123", database="face_recognizer")
#             cursor = conn.cursor()
#             cursor.execute("SELECT Std_id, Name, Roll, Dep FROM student")
#             data = {str(row[0]): {"Name": row[1], "Roll": row[2], "Dep": row[3]} for row in cursor.fetchall()}
#             conn.close()
#             return data

#         def draw_boundary(img, classifier, clf, student_data):
#             """Draw boundaries around detected faces and annotate with student details."""
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=10)
#             for (x, y, w, h) in features:
#                 face_id, predict = clf.predict(gray_image[y:y+h, x:x+w])
#                 confidence = int(100 * (1 - predict / 300))

#                 if confidence > 50:
#                     student_info = student_data.get(str(face_id), None)
#                     if student_info:
#                         name, roll, dep = student_info["Name"], student_info["Roll"], student_info["Dep"]
#                         cv2.putText(img, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                         cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                         cv2.putText(img, f"Department: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     else:
#                         cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
#                 else:
#                     cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)


#         def recognize_faces(video_cap, faceCascade, clf, student_data):
#             """Recognize faces in real-time."""
#             while True:
#                 ret, img = video_cap.read()
#                 if not ret:
#                     print("Failed to capture video frame")
#                     break

#                 draw_boundary(img, faceCascade, clf, student_data)
#                 cv2.imshow("Welcome To Face Recognition", img)

#                 if cv2.waitKey(1) == 13:  # Press 'Enter' key to exit
#                     break

#         # Load Haar Cascade
#         cascade_path = "haarcascade_frontalface_default.xml"
#         if not os.path.exists(cascade_path):
#             messagebox.showerror("Error", f"Haar Cascade file '{cascade_path}' is missing")
#             return
#         faceCascade = cv2.CascadeClassifier(cascade_path)

#         # Load Classifier
#         model_path = "classifier.xml"
#         if not os.path.exists(model_path):
#             messagebox.showerror("Error", f"Classifier file '{model_path}' is missing")
#             return
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read(model_path)

#         # Fetch student data
#         student_data = fetch_student_data()

#         # Start Video Capture
#         video_cap = cv2.VideoCapture(0)
#         recognize_faces(video_cap, faceCascade, clf, student_data)

#         # Release Resources
#         video_cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FaceRecognition(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import messagebox, Button
# from PIL import Image, ImageTk
# import mysql.connector
# import cv2
# import os

# class FaceRecognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         title_lbl = tk.Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         # Load left image
#         img_left_path = r"C:\\Users\\princ\\OneDrive\\Desktop\\Frontend Developer\\Face-recongnition_system\\facephoto1.jpg"
#         if os.path.exists(img_left_path):
#             img_left = Image.open(img_left_path).resize((650, 700), Image.LANCZOS)
#             self.photoimg_left = ImageTk.PhotoImage(img_left)
#             f_lbl_top = tk.Label(self.root, image=self.photoimg_left)
#             f_lbl_top.place(x=0, y=55, width=650, height=700)
#         else:
#             messagebox.showerror("Error", f"Image path '{img_left_path}' does not exist")

#         # Load right image
#         img_right_path = r"C:\\Users\\princ\\OneDrive\\Desktop\\Frontend Developer\\Face-recongnition_system\\facephoto2.webp"
#         if os.path.exists(img_right_path):
#             img_right = Image.open(img_right_path).resize((870, 700), Image.LANCZOS)
#             self.photoimg_right = ImageTk.PhotoImage(img_right)
#             f_lbl_right = tk.Label(self.root, image=self.photoimg_right)
#             f_lbl_right.place(x=650, y=55, width=870, height=700)
#         else:
#             messagebox.showerror("Error", f"Image path '{img_right_path}' does not exist")

#         # Face recognition button
#         b1_1 = Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2", 
#                       font=("times new roman", 18, "bold"), bg="red", fg="white")
#         b1_1.place(x=960, y=675, width=250, height=35)

#     def face_recog(self):
#         def fetch_student_data():
#             """Fetch all student data from the database and return as a dictionary."""
#             conn = mysql.connector.connect(host="localhost", username="root", password="Sachin@123", database="face_recognizer")
#             my_cursor = conn.cursor()
#             my_cursor.execute("SELECT Std_id, Name, Roll, Dep FROM student")
#             data = my_cursor.fetchall()
#             conn.close()
#             student_data = {}
#             for row in data:
#                 student_data[str(row[0])] = {"Name": row[1], "Roll": row[2], "Dep": row[3]}
#             return student_data

#         def draw_boundary(img, classifier, clf, student_data):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=10)

#             for (x, y, w, h) in features:
#                 face_id, predict = clf.predict(gray_image[y:y+h, x:x+w])
#                 confidence = int(100 * (1 - predict / 300))
#                 print(f"Predicted ID: {face_id}, Confidence: {confidence}")

#                 if confidence > 40:  # Adjust threshold for better results
#                     student_info = student_data.get(str(face_id), None)
#                     if student_info:
#                         name, roll, dep = student_info["Name"], student_info["Roll"], student_info["Dep"]
#                         cv2.putText(img, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                         cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                         cv2.putText(img, f"Department: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     else:
#                         print(f"Unknown face ID: {face_id}")
#                         cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
#                 else:
#                     print("Confidence too low")
#                     cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

#         def recognize(img, clf, faceCascade, student_data):
#             draw_boundary(img, faceCascade, clf, student_data)
#             return img

#         # Load Haar Cascade
#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#         # Load the pre-trained model
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")

#         # Fetch student data from database
#         student_data = fetch_student_data()

#         # Start video capture
#         video_cap = cv2.VideoCapture(0)

#         while True:
#             ret, img = video_cap.read()
#             if not ret:
#                 print("Failed to capture video frame")
#                 break

#             img = recognize(img, clf, faceCascade, student_data)
#             cv2.imshow("Welcome To Face Recognition", img)

#             if cv2.waitKey(1) == 13:  # Press 'Enter' key to exit
#                 break

#         video_cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     root = tk.Tk()
#     obj = FaceRecognition(root)
#     root.mainloop()