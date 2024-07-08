# main.py

import os
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.filemanager import MDFileManager
from PyPDF2 import PdfReader

class PDFToTextConverter(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        screen = MDScreen()
        
        self.file_path = MDTextField(
            hint_text="PDF File Path",
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            size_hint_x=None,
            width=300
        )
        screen.add_widget(self.file_path)
        
        select_button = MDRaisedButton(
            text="Select PDF",
            pos_hint={'center_x': 0.3, 'center_y': 0.6},
            on_release=self.open_file_manager
        )
        screen.add_widget(select_button)
        
        convert_button = MDRaisedButton(
            text="Convert to Text",
            pos_hint={'center_x': 0.7, 'center_y': 0.6},
            on_release=self.convert_pdf_to_text
        )
        screen.add_widget(convert_button)
        
        self.result_label = MDLabel(
            text="",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        screen.add_widget(self.result_label)
        
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path
        )
        
        return screen
    
    def open_file_manager(self, *args):
        self.file_manager.show('/')
    
    def exit_file_manager(self, *args):
        self.file_manager.close()
    
    def select_path(self, path):
        self.file_path.text = path
        self.exit_file_manager()
    
    def convert_pdf_to_text(self, *args):
        pdf_path = self.file_path.text
        if not pdf_path or not pdf_path.lower().endswith('.pdf'):
            self.result_label.text = "Please select a valid PDF file."
            return
        
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            output_path = pdf_path[:-4] + ".txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            
            self.result_label.text = f"Conversion successful!\nSaved as: {output_path}"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    PDFToTextConverter().run()
