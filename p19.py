import tkinter as tk

def create_face():
    window = tk.Tk()
    window.title("Simple Face")

    canvas_width = 300
    canvas_height = 300
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Head (Oval)
    head_center_x = canvas_width / 2
    head_center_y = canvas_height / 2
    head_radius_x = 100
    head_radius_y = 120
    canvas.create_oval(head_center_x - head_radius_x, head_center_y - head_radius_y,
                       head_center_x + head_radius_x, head_center_y + head_radius_y,
                       outline="green", width=3)

    # Left Eye (Circle)
    left_eye_center_x = head_center_x - 40
    left_eye_center_y = head_center_y - 50
    eye_radius = 20
    canvas.create_oval(left_eye_center_x - eye_radius, left_eye_center_y - eye_radius,
                       left_eye_center_x + eye_radius, left_eye_center_y + eye_radius,
                       fill="red")

    # Right Eye (Circle)
    right_eye_center_x = head_center_x + 40
    right_eye_center_y = head_center_y - 50
    canvas.create_oval(right_eye_center_x - eye_radius, right_eye_center_y - eye_radius,
                       right_eye_center_x + eye_radius, right_eye_center_y + eye_radius,
                       fill="blue")

    # Mouth (Rectangle)
    mouth_start_x = head_center_x - 50
    mouth_start_y = head_center_y + 20
    mouth_width = 100
    mouth_height = 20
    canvas.create_rectangle(mouth_start_x, mouth_start_y,
                             mouth_start_x + mouth_width, mouth_start_y + mouth_height,
                             fill="yellow")

    # Nose (Triangle - using Polygon)
    nose_point1_x = head_center_x
    nose_point1_y = head_center_y + 50
    nose_point2_x = head_center_x - 25
    nose_point2_y = head_center_y + 80
    nose_point3_x = head_center_x + 25
    nose_point3_y = head_center_y + 80
    canvas.create_polygon(nose_point1_x, nose_point1_y,
                             nose_point2_x, nose_point2_y,
                             nose_point3_x, nose_point3_y,
                             fill="black")

    window.mainloop()

if __name__ == "__main__":
    create_face()

