import customtkinter as ctk
import styles, exhibit_one, exhibit_two, exhibit_three, exhibit_four

values = {"Jet Black": "#31393C", "Light Blue": "#CDF7FF", "Pale Slate": "#BFBCCB", "Thistle": "#E7E0FF"}
def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def main():
    root = ctk.CTk()
    root.geometry("1920x1080+-5+0")
    root.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")
    
    foreground = styles.Foreground(root, fg_color=values["Jet Black"], border_color=from_rgb((255,255,255)))
    foreground.show()

    titleframe = styles.TitleFrame(foreground.foreground, fg_color=values["Thistle"], border_color=from_rgb((0,0,0)), sizex=1500, sizey=150)
    titleframe.show(x=800, y=125)

    title = styles.OutputText(titleframe.title, "Portfolio", text_color=values["Jet Black"])
    title.show()

    x = styles.ExitButton(foreground.foreground, root)
    x.show(border_color=from_rgb((0,0,0)), inner_color=from_rgb((255,255,255)), bg_color=values["Jet Black"], x=1660, y=125)


    A = styles.Button(foreground.foreground,"Exhibit A",lambda: exhibit_one.display(),values["Thistle"],from_rgb((0,0,0)),from_rgb((200,200,255)),75,values["Jet Black"],sizex=750,sizey=250)
    A.show(500,450)

    B = styles.Button(foreground.foreground,"Exhibit B",lambda: exhibit_two.display(),values["Thistle"],from_rgb((0,0,0)),from_rgb((200,200,255)),75,values["Jet Black"],sizex=750,sizey=250)
    B.show(1300,450)

    C = styles.Button(foreground.foreground,"Exhibit C",lambda: exhibit_three.display(),values["Thistle"],from_rgb((0,0,0)),from_rgb((200,200,255)),75,values["Jet Black"],sizex=750,sizey=250)
    C.show(500,750)

    D = styles.Button(foreground.foreground,"Exhibit D",lambda: exhibit_four.display(),values["Thistle"],from_rgb((0,0,0)),from_rgb((200,200,255)),75,values["Jet Black"],sizex=750,sizey=250)
    D.show(1300,750)

    root.mainloop()

main()