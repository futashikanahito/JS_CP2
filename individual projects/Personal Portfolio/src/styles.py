# -------- COPIED FROM ANOTHER PROJECT --------

# Imports
import customtkinter as ctk
from tkextrafont import Font
from PIL import Image
import os, random

# Load fonts
_font_loaded_roots = set()
def load_font(root):
    root_id = id(root)
    if root_id not in _font_loaded_roots:
        Font(file="csvs, txts, sprites/fonts/Dongle-Bold.ttf", family="Dongle", root=root)
        _font_loaded_roots.add(root_id)

class Foreground:
    def __init__(self, root, fg_color, border_color):
        self.root = root
        load_font(root)
        self.foreground = ctk.CTkFrame(
            master=root,
            border_width=10,
            corner_radius=100,
            border_color=border_color,
            fg_color=fg_color
        )
    
    def show(self):
        self.foreground.pack(pady=50, padx=50, fill="both", expand=True)


class TitleFrame:
    def __init__(self, foreground, fg_color, border_color, sizex=2000, sizey=150):
        self.title = ctk.CTkFrame(
            master=foreground,
            width=sizex,
            height=sizey,
            border_width=8,
            corner_radius=25,
            fg_color=fg_color,
            border_color=border_color,
        )
        self.sizex = sizex
        self.sizey = sizey
        
    def show(self, x=1100, y=150):
        self.title.place(x=x, y=y, anchor="center")
        self.title.configure(width=self.sizex, height=self.sizey)
        self.title.propagate(False)


class InputBox:
    def __init__(self, foreground, text, fg_color, border_color, text_color, text_size, sizex=1000, sizey=100):
        self.text_box = ctk.CTkEntry(
            master=foreground,
            width=sizex,
            height=sizey,
            border_width=5,
            corner_radius=10,
            fg_color=fg_color,
            border_color=border_color,
            placeholder_text=text,
            text_color=text_color,
            font=("Dongle", text_size)
        )
        self.sizex=sizex
        self.sizey=sizey
    
    def show(self, x, y):
        self.text_box.place(x=x, y=y, anchor="center")
        self.text_box.configure(width=self.sizex, height=self.sizey)
        self.text_box.propagate(False)
    
    def get_text(self):
        return self.text_box.get()


class Button:
    def __init__(self, foreground, text, command, fg_color, border_color, hover_color, text_size, text_color, sizex=1000, sizey=100):
        self.blue_button = ctk.CTkButton(
            master=foreground,
            width=sizex,
            height=sizey,
            border_width=10,
            corner_radius=25,
            border_color=border_color,
            fg_color=fg_color,
            hover_color=hover_color,
            text=text,
            text_color=text_color,
            command=command,
            font=("Dongle", text_size)
        )
        self.sizex = sizex
        self.sizey = sizey
    
    def show(self, x, y):
        self.blue_button.place(x=x, y=y, anchor="center")
        self.blue_button.configure(width=self.sizex, height=self.sizey)
        self.blue_button.propagate(False)


class ExitButton:
    def __init__(self, foreground, root):
        self.foreground = foreground
        self.root = root
    
    def show(self, border_color, inner_color, bg_color, x=2250, y=150):
        canvas = ctk.CTkCanvas(self.foreground, width=150, height=150, bg=bg_color, highlightthickness=0)
        
        def on_click(event):
            self.root.destroy()
            os.system("cls")

        canvas.place(x=x, y=y, anchor="center")

        border_width = 50
        inner_width = 30
        
        line1_coords = (125, 125, 25, 25) 
        line2_coords = (25, 125, 125, 25) 

        canvas.create_line(*line1_coords, fill=border_color, width=border_width, capstyle="round")
        canvas.create_line(*line2_coords, fill=border_color, width=border_width, capstyle="round")

        canvas.create_line(*line1_coords, fill=inner_color, width=inner_width, capstyle="round")
        canvas.create_line(*line2_coords, fill=inner_color, width=inner_width, capstyle="round")
        
        canvas.bind("<Button-1>", on_click)


class OutputText:
    def __init__(self, titleframe, text, text_color, text_size=100):
        self.text = ctk.CTkLabel(
            master=titleframe,
            text=text,
            font=("Dongle", text_size),
            text_color=text_color
        )

    def show(self):
        self.text.pack(pady=10)


class NewFrame:
    def __init__(self, foreground, fg_color, border_color, sizex, sizey):
        self.frame = ctk.CTkFrame(
            master=foreground,
            border_width=5,
            corner_radius=15,
            border_color=border_color,
            fg_color=fg_color
        )
        self.sizex=sizex
        self.sizey=sizey

    def show(self, x, y):
        self.frame.place(x=x, y=y, anchor="center")  
        self.frame.configure(width=self.sizex, height=self.sizey)
        self.frame.propagate(False)


class Notification:
    def __init__(self, foreground, border_color, fg_color, width=800, height=75):
        self.frame = ctk.CTkFrame(
            master=foreground,
            border_width=5,
            corner_radius=15,
            width=10,
            height=height,
            border_color=border_color,
            fg_color=fg_color
        )
        self.sizex = width
        self.sizey = height

    def show(self):
        self.start_y = 1500
        self.end_y = 1200
        self.step = 0
        self._animate()

    def _animate(self):
        if self.step < 30:
            t = self.step / 30
            eased = 1 - (1 - t) ** 3
            current_y = self.start_y + (self.end_y - self.start_y) * eased
            self.frame.place(x=int(1280), y=int(current_y), anchor="center")
            self.frame.configure(width=int(10), height=int(self.sizey))
            self.frame.propagate(False)

        elif self.step < 60:
            t = (self.step - 30) / 30
            eased = 1 - (1 - t) ** 3
            current_width = self.sizex * eased
            self.frame.configure(width=int(current_width))

        elif self.step < 160:
            pass

        elif self.step < 190:
            t = (self.step - 160) / 30
            eased = 1 - (1 - t) ** 3
            current_width = self.sizex * (1 - eased)
            self.frame.configure(width=int(max(current_width, 10)))

        elif self.step < 220:
            t = (self.step - 190) / 30
            eased = 1 - (1 - t) ** 3
            current_y = self.end_y + (self.start_y - self.end_y) * eased
            self.frame.place(x=int(1280), y=int(current_y), anchor="center")

        else:
            self.frame.place_forget()
            return

        self.step += 1
        self.frame.after(16, self._animate)


class ShowPicture:
    def __init__(self, image, dimension_x, dimension_y):
        def keep_on_top(root):
            root.lift()
            root.attributes("-topmost", True)
            root.after(50, keep_on_top, root)
        root = ctk.CTkToplevel()
        x = int(random.randint(500, 2060))
        y = int(random.randint(500, 940))
        root.geometry(f"{dimension_x}x{dimension_y}+{x}+{y}")
        root.resizable(False, False)

        root.attributes("-topmost", True)
        root.lift()
        root.focus_force()
        root.overrideredirect(True)

        pil_image = Image.open(image)
        ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(dimension_x, dimension_y))

        image_label = ctk.CTkLabel(root, image=ctk_image, text="")
        image_label.pack(expand=True, fill="both")
        image_label.bind("<Button-1>", lambda e: root.destroy())

        keep_on_top(root)


class SegmentedButton:
    def __init__(self, foreground, command, default, options=[]):
        self.segmented_button = ctk.CTkSegmentedButton(foreground, values=options, command=command)
        self.segmented_button.set(options[0] if options else default)
    
    def get_option(self):
        return self.segmented_button.get()
    
    def show(self):
        self.segmented_button.pack(pady=10)