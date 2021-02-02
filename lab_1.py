import tkinter as tk
from matplotlib import pyplot as plt


def plot_graph(points, title='Graph Plot'):
    plt.plot([p.x for p in points], [p.y for p in points], marker='o')
    for p in points:
        plt.text(p.x, p.y, '({}, {})'.format(p.x, p.y))
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title(title)
    plt.show()


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def plot(self):
        plot_graph([self])


class LineSegment:

    def __init__(self, start, end):
        # takes point object as start and end
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.start.__str__()} ---- {self.end.__str__() }"

    def points(self):
        return [self.start, self.end]

    def plot(self):
        plot_graph(self.points())


class Ray:

    def __init__(self, view_point, through_point, end_point):
        self.view_point = view_point
        self.through_point = through_point
        self.end_point = end_point

    def points(self):
        return [self.view_point, self.through_point, self.end_point]

    def plot(self):
        plot_graph(self.points())

    def __str__(self):
        return f"{self.view_point.__str__()} ---- {self.through_point.__str__() }"


def draw_point_canvas(root):

    point_canvas = tk.Canvas(root, width=700, height=250, relief='raised')
    point_canvas.pack()

    point_title = tk.Label(root, text='Drawing the Point', font=('helvetica', 18, 'bold'))
    point_canvas.create_window(200, 25, window=point_title)

    label_coordinate = tk.Label(root, text='Point', font=('helvetica', 14))
    point_canvas.create_window(80, 130, window=label_coordinate)

    x_label = tk.Label(root, text='X', font=('helvetica', 14))
    y_label = tk.Label(root, text='Y', font=('helvetica', 14))
    x_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    y_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    point_canvas.create_window(200, 100, window=x_label)
    point_canvas.create_window(400, 100, window=y_label)
    point_canvas.create_window(200, 130, window=x_entry)
    point_canvas.create_window(400, 130, window=y_entry)

    error_label = tk.Label(root, font=('Verdana', 14), fg='red')
    point_canvas.create_window(200, 170, window=error_label)

    def plot_point():
        try:
            x, y = int(x_entry.get()), int(y_entry.get())
        except Exception as e:
            error_label.config(text="Enter valid coordinates")
        else:
            error_label.config(text='')
            p = Point(x, y)
            p.plot()

    point_button = tk.Button(text='Plot', bg='black', fg='white', command=plot_point,
                             font=('helvetica', 9, 'bold'))
    point_canvas.create_window(500, 130, window=point_button)


def draw_line_canvas(root):
    line_canvas = tk.Canvas(root, width=700, height=250, relief='raised')
    line_canvas.pack()

    line_title = tk.Label(root, text='Drawing the Line', font=('helvetica', 18, 'bold'))
    line_canvas.create_window(200, 25, window=line_title)

    label_first = tk.Label(root, text='First Point', font=('helvetica', 14))
    line_canvas.create_window(80, 130, window=label_first)

    label_second = tk.Label(root, text='Last Point', font=('helvetica', 14))
    line_canvas.create_window(80, 180, window=label_second)

    x_label = tk.Label(root, text='X', font=('helvetica', 14))
    y_label = tk.Label(root, text='Y', font=('helvetica', 14))
    start_x_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    start_y_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    end_x_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    end_y_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    line_canvas.create_window(200, 100, window=x_label)
    line_canvas.create_window(400, 100, window=y_label)
    line_canvas.create_window(200, 130, window=start_x_entry)
    line_canvas.create_window(400, 130, window=start_y_entry)
    line_canvas.create_window(200, 180, window=end_x_entry)
    line_canvas.create_window(400, 180, window=end_y_entry)

    error_label = tk.Label(root, font=('Verdana', 14), fg='red')
    line_canvas.create_window(200, 210, window=error_label)

    def plot_line():
        try:
            x1, y1 = int(start_x_entry.get()), int(start_y_entry.get())
            x2, y2 = int(end_x_entry.get()), int(end_y_entry.get())
        except Exception as e:
            error_label.config(text="Enter valid coordinates")
        else:
            error_label.config(text='')
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            lseg = LineSegment(start=p1, end=p2)
            lseg.plot()

    line_button = tk.Button(text='Plot', bg='black', fg='white', command=plot_line,
                             font=('helvetica', 9, 'bold'))
    line_canvas.create_window(500, 130, window=line_button)


def draw_ray_canvas(root):
    ray_canvas = tk.Canvas(root, width=700, height=350, relief='raised')
    ray_canvas.pack()

    ray_title = tk.Label(root, text='Drawing the Ray', font=('helvetica', 18, 'bold'))
    ray_canvas.create_window(200, 25, window=ray_title)

    view_label = tk.Label(root, text='View Point', font=('helvetica', 14))
    ray_canvas.create_window(80, 130, window=view_label)

    through_label = tk.Label(root, text='Through Point', font=('helvetica', 14))
    ray_canvas.create_window(80, 180, window=through_label)

    end_label = tk.Label(root, text='End Point', font=('helvetica', 14))
    ray_canvas.create_window(80, 230, window=end_label)

    x_label = tk.Label(root, text='X', font=('helvetica', 14))
    y_label = tk.Label(root, text='Y', font=('helvetica', 14))
    view_x_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    view_y_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    through_x_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    through_y_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    end_x_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    end_y_entry = tk.Entry(root, width=10, font=('Verdana', 12))
    ray_canvas.create_window(200, 100, window=x_label)
    ray_canvas.create_window(400, 100, window=y_label)
    ray_canvas.create_window(200, 130, window=view_x_entry)
    ray_canvas.create_window(400, 130, window=view_y_entry)
    ray_canvas.create_window(200, 180, window=through_x_entry)
    ray_canvas.create_window(400, 180, window=through_y_entry)
    ray_canvas.create_window(200, 230, window=end_x_entry)
    ray_canvas.create_window(400, 230, window=end_y_entry)

    error_label = tk.Label(root, font=('Verdana', 14), fg='red')
    ray_canvas.create_window(200, 260, window=error_label)

    def plot_ray():
        try:
            x1, y1 = int(view_x_entry.get()), int(view_y_entry.get())
            x2, y2 = int(through_x_entry.get()), int(through_y_entry.get())
            x3, y3 = int(end_x_entry.get()), int(end_y_entry.get())
        except Exception as e:
            error_label.config(text="Enter valid coordinates")
        else:
            error_label.config(text='')
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            p3 = Point(x3, y3)
            ray = Ray(view_point=p1, through_point=p2, end_point=p3)
            ray.plot()

    ray_button = tk.Button(text='Plot', bg='black', fg='white', command=plot_ray,
                             font=('helvetica', 9, 'bold'))
    ray_canvas.create_window(500, 130, window=ray_button)


def main():
    root = tk.Tk()
    draw_point_canvas(root)
    draw_line_canvas(root)
    draw_ray_canvas(root)
    root.mainloop()
