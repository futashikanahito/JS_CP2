import customtkinter as ctk, importlib.util, sys, os, subprocess
import styles

folder_path = r"C:\Users\strat\JS_CP2\individual projects\fractal pattern generator"
file_path = os.path.join(folder_path, "main.py")

if folder_path not in sys.path:
    sys.path.append(folder_path)

spec = importlib.util.spec_from_file_location("fractal_main", file_path)
fractal_module = importlib.util.module_from_spec(spec)
sys.modules["fractal_main"] = fractal_module


values = {"Jet Black": "#31393C", "Light Blue": "#CDF7FF", "Pale Slate": "#BFBCCB", "Thistle": "#E7E0FF"}
def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def display():
    destination = [None]

    def go_back():
        destination[0] = "menu"
        root.withdraw()
        root.quit()

    def run():
        root.withdraw()
        proc = subprocess.Popen([sys.executable, file_path], cwd=folder_path)
        proc.wait()
        root.deiconify()
    
    root = ctk.CTk()
    root.geometry("1920x1080+-5+0")
    root.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")
    
    foreground = styles.Foreground(root, fg_color=values["Jet Black"], border_color=from_rgb((255,255,255)))
    foreground.show()

    titleframe = styles.TitleFrame(foreground.foreground, fg_color=values["Light Blue"], border_color=from_rgb((0,0,0)), sizex=1500, sizey=150)
    titleframe.show(x=800, y=125)

    title = styles.OutputText(titleframe.title, "Exhibit A", text_color=values["Jet Black"])
    title.show()

    x = styles.ExitButton(foreground.foreground, root, on_exit=go_back)
    x.show(border_color=from_rgb((0,0,0)), inner_color=from_rgb((255,255,255)), bg_color=values["Jet Black"], x=1660, y=125)


    text_box = styles.NewFrame(foreground.foreground, fg_color=values["Light Blue"], border_color=from_rgb((0,0,0)), sizex=1200, sizey=550)
    text_box.show(x=800, y=600)

    text = styles.OutputText(text_box.frame, text_color=from_rgb((0,0,0)), text_size=60, justify="left", text="Fractal Pattern Generator\nI remember in class when everyone else was struggling with\nthis project.\n That included me!\nEven though what I got done barely met the requirements, it's\nstill one of my favorite/most proud of projects I have ever made.")
    text.show()

    run_btn = styles.Button(foreground.foreground,text="R\nU\nN",command=run,fg_color=values["Light Blue"],border_color=from_rgb((0,0,0)),hover_color=from_rgb((200,200,255)),text_size=75,text_color=values["Jet Black"],sizex=20,sizey=50)
    run_btn.show(x=1600, y=600)

    root.mainloop()
    return destination[0]