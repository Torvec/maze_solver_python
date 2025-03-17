from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_btm_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_btm_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        origin_center_x = (self._x1 + self._x2) // 2
        origin_center_y = (self._y1 + self._y2) // 2
        dest_center_x = (to_cell._x1 + to_cell._x2) // 2
        dest_center_y = (to_cell._y1 + to_cell._y2) // 2
        
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        line = Line(Point(origin_center_x, origin_center_y), Point(dest_center_x, dest_center_y))
        self._win.draw_line(line, fill_color)

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c2 = Cell(win)
    c3 = Cell(win)
    c1.draw(300, 300, 400, 400)
    c2.draw(450, 300, 550, 400)
    c3.draw(200, 200, 300, 300)
    c1.draw_move(c2)
    c2.draw_move(c3)
    c1.draw_move(c3)
    
    win.wait_for_close()

if __name__ == '__main__':
    main()