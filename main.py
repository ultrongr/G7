import tkinter as tk

size = 10
teams = ["red", "yellow", "black", "green"]
listofmoves = []
Clicks = []
Days = -0.5


class Piece:
    def __init__(self, name, team, x, y):
        self.name = name
        self.team = team
        self.set_cords(x, y)
        self.speed_boost = 0
        self.power_boost = 0
        self.x, self.y = None, None

    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def move_piece(self, x1, y1):
        self.speed_boost = 0
        self.get_boosts()
        self.speed = (6 - int(self.name)) + self.speed_boost
        elegxos = 0
        if x1 == 6 and y1 == 6:
            elegxos = 1

        for piece in teams.katalog:
            if piece.x == x1 and piece.y == y1:
                if piece.team == self.team:
                    elegxos = 1
                    break

        if x1 == self.x:
            for piece in teams.katalog:
                if (piece.y in range(self.y + 1, y1) or piece.y in range(y1 + 1, self.y)) and x1 == piece.x:
                    elegxos = 1
                    break
            if elegxos == 0:
                if abs(y1 - self.y) <= self.speed:
                    self.y = y1
            else:
                invalid()

        if y1 == self.y:
            for piece in teams.katalog:
                if (piece.x in range(self.x + 1, x1) or piece.x in range(x1 + 1, self.x)) and y1 == piece.y:
                    elegxos = 1
                    break
            if elegxos == 0:
                if abs(x1 - self.x) <= self.speed:
                    self.x = x1
            else:
                invalid()
        for enemy in teams.katalog:
            if enemy.team != self.team:
                if self.x == enemy.x and self.y == enemy.y:
                    self.attack(enemy)

    def attack(self, enemy):
        self.power_boost = 0
        self.get_boosts()
        self.power = int(self.name) + self.power_boost
        enemy.attacked(self)

    def attacked(self, enemy):
        self.power_boost = 0
        self.get_boosts()
        self.power = int(self.name) + self.power_boost

        if self.power <= enemy.power:
            teams.katalog.remove(self)
            del self

        else:
            teams.katalog.remove(enemy)
            del enemy

    def get_boosts(self):
        for emperor in teams.katalog:
            if emperor.name in ("power", "speed", "average"):
                if emperor.team == self.team:
                    if emperor.throne == 1:
                        if emperor.name == "power":
                            self.speed_boost = 0
                            self.power_boost = 2
                        elif emperor.name == "speed":
                            self.power_boost = 0
                            self.speed_boost = 2
                        elif emperor.name == "average":
                            self.speed_boost = 1
                            self.power_boost = 1
                        else:
                            self.power_boost = 0
                            self.speed_boost = 0


class Emperors():
    def __init__(self, name, team, x, y):
        self.name = name
        self.team = team
        self.set_cords(x, y)
        self.days = 0
        self.throne = 0

    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def move_piece(self, x1, y1):
        self.speed = 1
        elegxos = 0
        if (x1 == 5 or x1 == 7) and (y1 == 5 or y1 == 7):
            elegxos = 1
        if elegxos == 0:
            if abs(self.y - y1) <= self.speed and abs(self.x - x1) <= self.speed:
                if self.team == "red":
                    if (self.x, self.y) == (0, 0):
                        self.throne = 0
                    elif (x1, y1) == (0, 0):
                        self.throne = 1
                elif self.team == "yellow":
                    if (self.x, self.y) == (12, 12):
                        self.throne = 0
                    elif (x1, y1) == (12, 12):
                        self.throne = 1

                self.x = x1
                self.y = y1
        else:
            invalid()

        for enemy in teams.katalog:
            if enemy != self:
                if enemy.x == self.x and enemy.y == self.y:
                    self.attack(enemy)

    def attacked(self, enemy):
        teams.katalog.remove(self)
        del self

    def attack(self, enemy):
        teams.katalog.remove(enemy)
        del enemy


class Canons():
    def __init__(self, name, team, x, y, direction):
        self.name = name
        self.team = team
        self.set_cords(x, y, direction)

    def set_cords(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move_piece(self, list_of_moves):
        print(list_of_moves)
        self.shot = 0
        elegxos = 0
        self.moved = 0
        for x in list_of_moves:
            print("=")
            if x == "move":
                x1 = self.x + int(self.direction[0:2]) * 1
                y1 = self.y + int(self.direction[2:4]) * 1
                if len(list_of_moves) > 1:
                    if self.moved == 0:
                        if list_of_moves == ["move", "move"]:
                            self.moved = 1
                            x2 = self.x + int(self.direction[0:2]) * 2
                            y2 = self.y + int(self.direction[2:4]) * 2
                            for piece in teams.katalog:
                                if piece.x == x2 and piece.y == y2:
                                    if piece.team == self.team:
                                        elegxos = 1
                                        break

                for piece in teams.katalog:
                    if piece.x == x1 and piece.y == y1:
                        if piece.team == self.team:
                            elegxos = 1
                            break
                print(100 * elegxos)
                print(self.x, self.y)
                if elegxos == 0:
                    self.x = x1
                    self.y = y1
                else:
                    invalid()

            dictcw = {"+1+0": "+0+1", "+0+1": "-1+0", "-1+0": "+0-1", "+0-1": "+1+0"}
            dictccw = {"+0+1": "+1+0", "-1+0": "+0+1", "+0-1": "-1+0", "+1+0": "+0-1"}
            if x == "turncw":
                elegxos = 0
                if list_of_moves[-1] == "move":
                    x2 = self.x + int(dictcw[self.direction][0:2]) * 1
                    y2 = self.y + int(dictcw[self.direction][2:4]) * 1
                    for piece in teams.katalog:
                        if piece.x == x2 and piece.y == y2:
                            if piece.team == self.team:
                                elegxos = 1
                                break
                if elegxos == 0:
                    self.direction = dictcw[self.direction]
                else:
                    invalid()
            if x == "turnccw":
                elegxos = 0
                if list_of_moves[-1] == "move":
                    x2 = self.x + int(dictccw[self.direction][0:2]) * 1
                    y2 = self.y + int(dictccw[self.direction][2:4]) * 1
                    print(x2, y2, elegxos)
                    for piece in teams.katalog:
                        if piece.x == x2 and piece.y == y2:
                            if piece.team == self.team:
                                elegxos = 1
                                break
                if elegxos == 0:
                    self.direction = dictccw[self.direction]
                else:
                    invalid()
            if x == "shoot":
                if self.shot == 0:
                    self.shot = 1
                    self.attack(self.x, self.y)
                else:
                    self.attack(self.x + int(self.direction[:2]) * 3, self.y + int(self.direction[2:4]) * 3)

    def attacked(self, enemy):
        teams.katalog.remove(self)
        del self

    def attack(self, x1, y1):
        self.power = 10
        for x in range(x1 + int(self.direction[:2]), x1 + int(self.direction[:2]) * 4):
            for enemy in teams.katalog:
                if enemy != self:
                    if x == enemy.x and y1 == enemy.y:
                        teams.katalog.remove(enemy)
                        del enemy
        for x in range(x1 + int(self.direction[:2]) * 3, x1):
            for enemy in teams.katalog:
                if enemy != self:
                    if x == enemy.x and y1 == enemy.y:
                        teams.katalog.remove(enemy)
                        del enemy

        for y in range(y1 + int(self.direction[2:4]), y1 + int(self.direction[2:4]) * 4):
            for enemy in teams.katalog:
                if enemy != self:
                    if x1 == enemy.x and y == enemy.y:
                        teams.katalog.remove(enemy)
                        del enemy
        for y in range(y1 + int(self.direction[2:4]) * 3, y1):
            for enemy in teams.katalog:
                if enemy != self:
                    if x1 == enemy.x and y == enemy.y:
                        teams.katalog.remove(enemy)
                        del enemy


class Teams():
    def __init__(self):
        self.katalog = []
        self.create_red()
        self.create_yellow()
        # piece = Piece("5.1", "red", 0, 0)
        # katalogos.append(piece)

    def create_red(self):
        piece = Piece("5", "red", 0, 0)
        self.katalog.append(piece)
        emperor = Emperors("power", "red", 1, 0)
        self.katalog.append(emperor)
        emperor = Emperors("speed", "red", 0, 1)
        self.katalog.append(emperor)
        emperor = Emperors("average", "red", 1, 1)
        self.katalog.append(emperor)
        canon = Canons("10", "red", 0, 2, "+0+1")
        self.katalog.append(canon)
        canon = Canons("10", "red", 2, 0, "+1+0")
        self.katalog.append(canon)
        piece = Piece("2", "red", 4, 0)
        self.katalog.append(piece)
        piece = Piece("2", "red", 3, 1)
        self.katalog.append(piece)
        piece = Piece("2", "red", 1, 3)
        self.katalog.append(piece)
        piece = Piece("2", "red", 0, 4)
        self.katalog.append(piece)
        piece = Piece("4", "red", 0, 3)
        self.katalog.append(piece)
        piece = Piece("4", "red", 3, 0)
        self.katalog.append(piece)
        piece = Piece("1", "red", 2, 1)
        self.katalog.append(piece)
        piece = Piece("1", "red", 1, 2)
        self.katalog.append(piece)
        piece = Piece("1", "red", 2, 2)
        self.katalog.append(piece)
        piece = Piece("5", "red", 3, 3)
        self.katalog.append(piece)
        piece = Piece("3", "red", 4, 1)
        self.katalog.append(piece)
        piece = Piece("3", "red", 1, 4)
        self.katalog.append(piece)
        piece = Piece("3", "red", 3, 2)
        self.katalog.append(piece)
        piece = Piece("3", "red", 2, 3)
        self.katalog.append(piece)

    def create_yellow(self):
        piece = Piece("5", "yellow", 12, 12)
        self.katalog.append(piece)
        emperor = Emperors("power", "yellow", 11, 12)
        self.katalog.append(emperor)
        emperor = Emperors("speed", "yellow", 12, 11)
        self.katalog.append(emperor)
        emperor = Emperors("average", "yellow", 11, 11)
        self.katalog.append(emperor)
        canon = Canons("10", "yellow", 10, 12, "-1+0")
        self.katalog.append(canon)
        canon = Canons("10", "yellow", 12, 10, "+0-1")
        self.katalog.append(canon)
        piece = Piece("1", "yellow", 10, 10)
        self.katalog.append(piece)
        piece = Piece("1", "yellow", 10, 11)
        self.katalog.append(piece)
        piece = Piece("1", "yellow", 11, 10)
        self.katalog.append(piece)
        piece = Piece("5", "yellow", 9, 9)
        self.katalog.append(piece)
        piece = Piece("4", "yellow", 9, 12)
        self.katalog.append(piece)
        piece = Piece("4", "yellow", 12, 9)
        self.katalog.append(piece)
        piece = Piece("2", "yellow", 8, 12)
        self.katalog.append(piece)
        piece = Piece("2", "yellow", 12, 8)
        self.katalog.append(piece)
        piece = Piece("2", "yellow", 9, 11)
        self.katalog.append(piece)
        piece = Piece("2", "yellow", 11, 9)
        self.katalog.append(piece)
        piece = Piece("3", "yellow", 8, 11)
        self.katalog.append(piece)
        piece = Piece("3", "yellow", 11, 8)
        self.katalog.append(piece)
        piece = Piece("3", "yellow", 9, 10)
        self.katalog.append(piece)
        piece = Piece("3", "yellow", 10, 9)
        self.katalog.append(piece)


teams = Teams()


def draw_board():
    del_window(root)
    for x in range(0, 13):
        for y in range(0, 13):
            bg = "#90DDCA"
            if (x <= 4 or x >= 8) and (y <= 1 or y >= 11):
                bg = "#857F34"
            if (x <= 3 or x >= 9) and (2 <= y <= 3 or 9 <= y <= 10):
                bg = "#857F34"
            if x in (0, 1, 11, 12) and (y == 4 or y == 8):
                bg = "#857F34"
            if (x == 0 or x == 12) and (y == 0 or y == 12):
                bg = "#4E4714"
            if (x == 5 or x == 7) and (y == 5 or y == 7):
                bg = "#24A7FF"
            if x == 6 and y == 6:
                bg = "#E2D209"

            canvas = tk.Canvas(root, bg=bg, height=50, width=50, highlightthickness=1)

            for piece in teams.katalog:
                if piece.x == x and piece.y == y:
                    if piece.name in ("12345"):
                        tk.Label(root, bg=bg, text=piece.name, bd=0, font="Arial 25", fg=piece.team).grid(row=piece.y,
                                                                                                          column=piece.x)

                    elif piece.name == "10":
                        (a, b, c, d, e, f, g) = (5, 15, 45, 35, 7, 20, 43)
                        if piece.direction == "+1+0":
                            canvas.create_rectangle(a, b, c, d, fill="black")
                            canvas.create_rectangle(a, e, f, b, fill="grey")
                            canvas.create_rectangle(a, d, f, g, fill="grey")
                        if piece.direction == "+0+1":
                            canvas.create_rectangle(b, a, d, c, fill="black")
                            canvas.create_rectangle(e, a, b, f, fill="grey")
                            canvas.create_rectangle(d, a, g, f, fill="grey")
                        if piece.direction == "-1+0":
                            canvas.create_rectangle(a, b, c, d, fill="black")
                            canvas.create_rectangle(50 - a, e, 50 - f, b, fill="grey")
                            canvas.create_rectangle(50 - a, d, 50 - f, g, fill="grey")
                        if piece.direction == "+0-1":
                            canvas.create_rectangle(b, a, d, c, fill="black")
                            canvas.create_rectangle(e, 50 - a, b, 50 - f, fill="grey")
                            canvas.create_rectangle(d, 50 - a, g, 50 - f, fill="grey")
                    else:
                        tk.Label(root, bg=bg, text=piece.name[0].upper(), bd=0, font="Arial 25", fg=piece.team).grid(
                            row=piece.y, column=piece.x)
                        bg = "black"
                        if piece.team == "red":
                            if piece.name == "power":
                                tk.Label(root, bg=bg, text="Power: " + str(piece.days) + " days", bd=0,
                                         font="Arial 25", fg=piece.team).grid(row=7, column=13)
                            if piece.name == "average":
                                tk.Label(root, bg=bg, text="Average : " + str(piece.days) + " days", bd=0,
                                         font="Arial 25", fg=piece.team).grid(row=8, column=13)
                            if piece.name == "speed":
                                tk.Label(root, bg=bg, text="Speed :" + str(piece.days) + " days", bd=0,
                                         font="Arial 25", fg=piece.team).grid(row=9, column=13)
                        if piece.team == "yellow":
                            if piece.name == "power":
                                tk.Label(root, bg=bg, text="Power: " + str(piece.days) + " days", bd=0,
                                         font="Arial 25", fg=piece.team).grid(row=10, column=13)
                            if piece.name == "average":
                                tk.Label(root, bg=bg, text="Average : " + str(piece.days) + " days", bd=0,
                                         font="Arial 25", fg=piece.team).grid(row=11, column=13)
                            if piece.name == "speed":
                                tk.Label(root, bg=bg, text="Speed :" + str(piece.days) + " days", bd=0,
                                         font="Arial 25", fg=piece.team).grid(row=12, column=13)

            canvas.grid(row=y, column=x)
    days()
    text = "Red's turn"
    fg = "red"
    if Days % 1 == 0:
        text = "Yellow's turn"
        fg = "yellow"
    tk.Label(root, bg=bg, text=text, bd=0, font="Arial 20", fg=fg).grid(row=0, column=14)


def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list


def del_window(root):
    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()


def move():
    global listofmoves
    listofmoves.append("move")


def rotateccw():
    global listofmoves
    listofmoves.append("turnccw")


def rotatecw():
    global listofmoves
    listofmoves.append("turncw")


def shoot():
    global listofmoves
    listofmoves.append("shoot")


def end():
    global listofmoves
    global canon1
    global Clicks
    Clicks = []
    if len(listofmoves) <= 2:
        canon1.move_piece(listofmoves)
    else:
        invalid()
    listofmoves = []
    draw_board()


def click(event):
    print(1)
    global Clicks
    global Days
    global listofmoves
    global canon1

    xa = root.winfo_pointerx() - root.winfo_rootx()
    ya = root.winfo_pointery() - root.winfo_rooty()
    x = xa // 52
    y = ya // 52
    Clicks.append((x, y))
    if len(Clicks) == 2:
        for piece in teams.katalog:
            if (piece.x, piece.y) == Clicks[0]:
                if (piece.team == "yellow" and Days % 1 == 0) or (piece.team == "red" and Days % 1 == 0.5):
                    if piece.name != "10":
                        piece.move_piece(Clicks[1][0], Clicks[1][1])
                        draw_board()
                        Clicks = []
                        break
                    else:
                        tk.Label(root, bg="green", text="Select the list of moves:", bd=0, font="Arial 20",
                                 fg="blue").grid(row=0, column=13)
                        tk.Button(root, bg="green", text="Move", command=move).grid(row=1, column=13)
                        tk.Button(root, bg="green", text="Rotate clockwise", command=rotatecw).grid(row=2, column=13)
                        tk.Button(root, bg="green", text="Rotate counter-clockwise", command=rotateccw).grid(row=3,
                                                                                                             column=13)
                        tk.Button(root, bg="green", text="Shoot", command=shoot).grid(row=4, column=13)
                        tk.Button(root, bg="green", text="End", command=end).grid(row=5, column=13)
                        canon1 = piece
                else:
                    invalid()


def click2(event):
    print(2)
    global Clicks
    Clicks = []


def win_check(event):
    print("c")
    for piece in teams.katalog:
        if piece.x == 6 and piece.y == 6:
            if piece.name in ("power", "average", "speed"):
                print("Κέρδισε η ομαδα ", piece.team)
    for piece1 in teams.katalog:
        if piece1.x == 5 and piece1.y == 5:
            for piece2 in teams.katalog:
                if piece2.x == 5 and piece2.y == 7 and piece1.team == piece2.team:
                    for piece3 in teams.katalog:
                        if piece3.x == 7 and piece3.y == 5 and piece3.team == piece2.team:
                            for piece4 in teams.katalog:
                                if piece4.x == 7 and piece4.y == 7 and piece4.team == piece2.team:
                                    print("Κέρδισε η ομάδα ", piece1.team)


def invalid():
    print("invalid move")


def days():
    global Days
    Days += 0.5
    if Days % 1 == 0:
        for emperor in teams.katalog:
            if emperor.name in ("power", "average", "speed"):
                if emperor.throne == 1:
                    emperor.days += 1
                    if emperor.days == 13:
                        teams.katalog.remove(emperor)
                        del emperor


root = tk.Tk()
root.geometry("1125x675+10+10")
draw_board()

root.bind("<a>", click)
root.bind("<Button-3>", click2)
root.bind("<c>", win_check)

root.mainloop()
