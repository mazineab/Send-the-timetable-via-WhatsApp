from flet import *
import os
import shutil
from codee import Code

def main(page:Page):
    page.title="App Ofppt"
    page.window_center()
    page.window_width=300
    page.window_height=600
    page.update()

    def save(e:FilePickerResultEvent):
        for x in e.files:
            you_copy=os.path.join(os.getcwd(),"img")
            shutil.copy(x.path,you_copy)
            page.update()

    file_picker=FilePicker(
        on_result=save
    )

    def save2(e:FilePickerResultEvent):
        for x in e.files:
            you_copy=os.path.join(os.getcwd(),"client")
            shutil.copy(x.path,you_copy)
            page.update()

    file_picker2=FilePicker(
        on_result=save2
    )

    page.overlay.append(file_picker)
    page.overlay.append(file_picker2)

    txt1=Text("Click to upload images",size=25,color=colors.WHITE)
    btn1=ElevatedButton("click",width=120,height=40,bgcolor=colors.WHITE,color=colors.LIGHT_BLUE_500,
                        on_click=lambda e:file_picker.pick_files(allow_multiple=True))


    txt2=Text("Click to upload file",size=25,color=colors.WHITE)
    btn2=ElevatedButton("click",width=120,height=40,bgcolor=colors.WHITE,color=colors.LIGHT_BLUE_500,
                        on_click=lambda e:file_picker2.pick_files())
    
    txt3=Text("Click to send image ",size=25,color=colors.WHITE)
    btn3=ElevatedButton("click",width=120,height=40,bgcolor=colors.WHITE,color=colors.RED_ACCENT,
                        on_click=Code.test)
    

    layoutVertical=Column(
        controls=[
            txt1,
            btn1,
            txt2,
            btn2,
            txt3,
            btn3
        ]
    )

    page.add(layoutVertical)

if "__main__"==__name__:
    app(main,upload_dir="upldimg")