from tkinter import *


class RunApp:
    start_score = 25000
    return_score = 30000
    oka = (return_score - start_score) * 4

    uma_4to1 = 20000
    uma_3to2 = 10000

    def __init__(self):
        window = Tk()
        window.title("점수 계산기")

        Label(window, text="동").grid(row=1, column=1, sticky=W)
        Label(window, text="남").grid(row=2, column=1, sticky=W)
        Label(window, text="서").grid(row=3, column=1, sticky=W)
        Label(window, text="북").grid(row=4, column=1, sticky=W)

        self.east_raw = StringVar()
        Entry(window, textvariable=self.east_raw, justify=RIGHT).grid(row=1, column=2)
        self.south_raw = StringVar()
        Entry(window, textvariable=self.south_raw, justify=RIGHT).grid(row=2, column=2)
        self.west_raw = StringVar()
        Entry(window, textvariable=self.west_raw, justify=RIGHT).grid(row=3, column=2)
        self.north_raw = StringVar()
        Entry(window, textvariable=self.north_raw, justify=RIGHT).grid(row=4, column=2)

        self.sum = StringVar()
        lbl_sum = Label(window, textvariable=self.sum).grid(row=5, column=2, sticky=E)

        self.east_end = StringVar()
        lbl_east_end = Label(window, textvariable=self.east_end).grid(row=1, column=3, sticky=E)
        self.south_end = StringVar()
        lbl_south_end = Label(window, textvariable=self.south_end).grid(row=2, column=3, sticky=E)
        self.west_end = StringVar()
        lbl_west_end = Label(window, textvariable=self.west_end).grid(row=3, column=3, sticky=E)
        self.north_end = StringVar()
        lbl_north_end = Label(window, textvariable=self.north_end).grid(row=4, column=3, sticky=E)

        btn_clear = Button(window, text="비우기", command=self.clear).grid(row=6, column=2, sticky=E)
        btn_calculate = Button(window, text="계산", command=self.calculate_scores).grid(row=6, column=3, sticky=E)

        window.mainloop()

    def clear(self):
        self.east_raw.set("")
        self.south_raw.set("")
        self.west_raw.set("")
        self.north_raw.set("")

    def calculate_scores(self):
        east = int(self.east_raw.get()) + 3
        south = int(self.south_raw.get()) + 2
        west = int(self.west_raw.get()) + 1
        north = int(self.north_raw.get()) + 0

        scores = [east, south, west, north]
        scores.sort()

        self.sum.set(east + south + west + north - 6)

        self.east_end.set(self.calculate_single_score(self.east_raw.get(), scores.index(east)))
        self.south_end.set(self.calculate_single_score(self.south_raw.get(), scores.index(south)))
        self.west_end.set(self.calculate_single_score(self.west_raw.get(), scores.index(west)))
        self.north_end.set(self.calculate_single_score(self.north_raw.get(), scores.index(north)))

    def calculate_single_score(self, raw_score, idx):
        raw_score = int(raw_score)
        if idx == 3:
            end_score = raw_score + self.uma_4to1 + self.oka
        elif idx == 2:
            end_score = raw_score + self.uma_3to2
        elif idx == 1:
            end_score = raw_score - self.uma_3to2
        elif idx == 0:
            end_score = raw_score - self.uma_4to1

        return (end_score - self.return_score) / 1000


RunApp()
