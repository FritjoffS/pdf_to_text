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
        self.theme_cls.theme_style = "Dark"
        
        screen = MDScreen()
        
        self.input_file_path = MDTextField(
            hint_text="Input PDF File Path",
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            size_hint_x=None,
            width=300
        )
        screen.add_widget(self.input_file_path)
        
        select_input_button = MDRaisedButton(
            text="Select PDF",
            pos_hint={'center_x': 0.3, 'center_y': 0.7},
            on_release=lambda x: self.open_file_manager('input')
        )
        screen.add_widget(select_input_button)
        
        self.output_file_path = MDTextField(
            hint_text="Output Text File Path",
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            size_hint_x=None,
            width=300
        )
        screen.add_widget(self.output_file_path)
        
        select_output_button = MDRaisedButton(
            text="Select Output",
            pos_hint={'center_x': 0.3, 'center_y': 0.5},
            on_release=lambda x: self.open_file_manager('output')
        )
        screen.add_widget(select_output_button)
        
        convert_button = MDRaisedButton(
            text="Convert to Text",
            pos_hint={'center_x': 0.7, 'center_y': 0.5},
            on_release=self.convert_pdf_to_text
        )
        screen.add_widget(convert_button)
        
        self.result_label = MDLabel(
            text="",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )
        screen.add_widget(self.result_label)
        
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path
        )
        
        self.file_manager_mode = 'input'
        
        return screen
    
    def open_file_manager(self, mode):
        self.file_manager_mode = mode
        if mode == 'input':
            self.file_manager.show('/')
        else:
            self.file_manager.show(os.path.expanduser('~'))
    
    def exit_file_manager(self, *args):
        self.file_manager.close()
    
    def select_path(self, path):
        if self.file_manager_mode == 'input':
            self.input_file_path.text = path
        else:
            dir_path = os.path.dirname(path)
            self.output_file_path.text = os.path.join(dir_path, 'output.txt')
        self.exit_file_manager()
    
    def convert_pdf_to_text(self, *args):
        pdf_path = self.input_file_path.text
        output_path = self.output_file_path.text
        
        if not pdf_path or not pdf_path.lower().endswith('.pdf'):
            self.result_label.text = "Please select a valid PDF file."
            return
        
        if not output_path:
            self.result_label.text = "Please select an output location."
            return
        
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            
            self.result_label.text = f"Conversion successful!\nSaved as: {output_path}"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    PDFToTextConverter().run()
