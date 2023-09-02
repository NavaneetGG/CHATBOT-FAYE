import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
import webbrowser
import math
import subprocess
from kivy.core.window import Window
import os
from kivy.core.audio import SoundLoader

kivy.require("1.11.1")

Window.clearcolor = ((0.75, 0.75, 0.5, 1))

class EducationalChatbotApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Hello! I'm Faye!,Feel free to ask me anything!",
                           size_hint_y=None, height=150, color=(0, 0, 0, 1), font_size=28)
        self.layout.add_widget(self.label)

        self.chat_history = ""

        self.background_image = Image(
            source='C:/Users/adiyo/OneDrive/Pictures/picture8.jpg', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.background_image)

        self.default_links_label = Label(
            text="Useful Shortcuts:", size_hint_y=None, height=30, color=(0, 0, 0, 1), font_size=19)
        self.layout.add_widget(self.default_links_label)

        self.default_links = BoxLayout(
            orientation='vertical', size_hint_y=None, height=150)
        self.default_links.add_widget(
            Button(text="GOOGLE", on_press=lambda x: self.open_web_page("https://www.google.com/")))
        self.default_links.add_widget(
            Button(text="YOUTUBE", on_press=lambda x: self.open_web_page("https://www.youtube.com/")))
        self.default_links.add_widget(
            Button(text="CBSE WEBSITE", on_press=lambda x: self.open_web_page("https://www.cbse.gov.in/")))
        self.default_links.add_widget(
            Button(text="NCERT WEBSITE", on_press=lambda x: self.open_web_page("https://ncert.nic.in/")))

        self.layout.add_widget(self.default_links)

        self.input = TextInput(
            hint_text="Describe your thoughts or questions here", multiline=False, size_hint_y=None, height=50)
        self.layout.add_widget(self.input)

        self.send_button = Button(
            text="Send", size_hint_y=None, height=50, background_color=(0, 0, 0, 1))
        self.send_button.bind(on_press=self.process_input)
        self.layout.add_widget(self.send_button)

        self.input.bind(on_text_validate=self.process_input)

        self.open_file_explorer_button = Button(
            text="Files", size_hint_y=None, height=50, background_color=(0, 0, 0, 1))
        self.open_file_explorer_button.bind(
            on_press=self.open_file_explorer)
        self.layout.add_widget(self.open_file_explorer_button)

        self.save_button = Button(
            text="Save Chat History", size_hint_y=None, height=50, background_color=(0, 0, 0, 1))
        self.save_button.bind(on_press=self.save_chat_history)
        self.layout.add_widget(self.save_button)
        self.sound = SoundLoader.load("C:/Users/adiyo/Downloads/Whatsapp Web Notification (Full HD).wav")

        return self.layout

    def process_input(self, instance):
        user_input = self.input.text
        response = self.generate_response(user_input)
        self.chat_history += f"You: {user_input}\nFaye: {response}\n\n"
        self.label.text = response
        self.input.text = ""


        if self.sound:
            self.sound.play()

    def open_web_page(self, url):
        webbrowser.open(url)

    def open_file_explorer(self, instance):
        try:
            subprocess.Popen(["explorer.exe"])
        except Exception as e:
            print("Error opening file explorer:", str(e))

    def calculate_area(self, shape, values):
        if shape == "rectangle" and len(values) == 2:
            return f"The area of the rectangle is {values[0] * values[1]}"
        elif shape == "circle" and len(values) == 1:
            return f"The area of the circle is {math.pi * values[0] ** 2}"
        elif shape == "triangle" and len(values) == 2:
            return f"The area of the triangle is {(values[0] * values[1]) / 2}"
        elif shape == "square" and len(values) == 1:
            return f"The area of the square is {(values[0] * values[0])}"
        else:
            return "Invalid input for calculating area."

    def calculate_perimeter(self, shape, values):
        if shape == "rectangle" and len(values) == 2:
            return f"The perimeter of the rectangle is {2 * (values[0] + values[1])}"
        elif shape == "circle" and len(values) == 1:
            return f"The circumference of the circle is {2 * math.pi * values[0]}"
        elif shape == "triangle" and len(values) == 3:
            return f"The perimeter of the triangle is {sum(values)}"
        elif shape == "square" and len(values) == 1:
            return f"The perimeter of the square is {(values[0] + values[0] + values[0] + values[0])}"
        else:
            return "Invalid input for calculating perimeter."

    def perform_arithmetic(self, expression):
        try:
            result = eval(expression)
            return f"The result of the expression '{expression}' is {result}"
        except:
            return "Invalid arithmetic expression"

    def generate_response(self, user_input):
        response = ""

        if any(greeting in user_input.lower() for greeting in ["hai", "hello", "hey"]):
            response = "Hey there! What can I do for you?"
        elif any(question in user_input.lower() for question in ["your", "name"]):
            response = "My name is Faye!!, but my makers call me Murph!"
        elif any(question in user_input.lower() for question in ["bye", "goodbye"]):
            response = "Byee see you around!!"
        elif all(question in user_input.lower() for question in ["can", "you", "do"]):
            response = "I will try my best to answer your questions as much as possible!"
        elif any(question in user_input.lower() for question in ["newtons first law"]):
            response = "Newton's first law states that every object will remain at rest or in uniform motion in a straight line unless compelled to change its state by the action of an external force"
        elif any(question in user_input.lower() for question in ["greatest", "footballer"]):
            response = "One and only Lionel Messi"
        elif all(question in user_input.lower() for question in ["unit", "coefficient of friction"]):
            response = "Since mass, velocity, and time all have zero dimensions, the coefficient of friction has no unit"
        elif any(question in user_input.lower() for question in ["modern periodic law"]):
            response = "Elements are arranged according to their physical and chemical properties and with the increase in atomic numbers."
        elif all(question in user_input.lower() for question in ["electronic configuration"]):
            response = "Electronic configuration defines how electrons are distributed into orbitals of an atom."
        elif all(question in user_input.lower() for question in ["define", "isotopes"]):
            response = "Isotopes are atoms of the same element with the same number of protons but different numbers of neutrons"
        elif all(question in user_input.lower() for question in ["law", "conservation of energy"]):
            response = "Energy cannot be created or destroyed; it can only be transferred or converted from one form to another."
        elif all(question in user_input.lower() for question in ["value", "sin 0"]):
            response = "The value of Sin 0 is 0"
        elif any(question in user_input.lower() for question in ["compiler", "programming"]):
            response = "A compiler translates the entire source code of a program into machine code, making the program executable"
        elif any(question in user_input.lower() for question in ["inertia"]):
            response = "Inertia is the tendency of an object to remain at rest or in uniform motion unless acted upon by an external force."
        elif all(question in user_input.lower() for question in ["value", "cos π"]):
            response = "The value of Cos π is -1"
        elif any(question in user_input.lower() for question in ["covalent bond."]):
            response = "A covalent bond is a chemical bond formed by the sharing of electrons between atoms."
        elif all(question in user_input.lower() for question in ["value", "cot 0"]):
            response = "The value of cot(0) is undefined"
        elif any(question in user_input.lower() for question in ["s block"]):
            response = """Because of high reactivity they are never found pure in nature,
They lose the outermost electron(s) readily to form 1+ ion (in the case of alkali metals) or
2+ion (in the case of alkaline earth metals).
"""
        elif all(question in user_input.lower() for question in ["p", "block"]):
            response = """The outermost electronic configuration varies from ns2np1 to ns2np6 in each period,.
All the orbitals in the valence shell of the noble gases are completely filled by electrons and
it is very difficult to alter this stable arrangement by the addition or removal of electrons
"""
        elif all(question in user_input.lower() for question in ["d", "block"]):
            response = """They mostly form coloured ions, exhibit variable valence (oxidation states), paramagnetism and oftenly used as catalysts,
These elements have the general outer electronic configuration(n-1)d1-10ns0-2 except for Pd where its electronic configuration is 4d105s0.
"""
        elif all(question in user_input.lower() for question in ["f", "block"]):
            response = "f-block elements have high melting and boiling points,series of elements are hence called the InnerTransition Elements (f-Block Elements)."
        elif all(question in user_input.lower() for question in ["what", "computer"]):
            response = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically."
        elif all(question in user_input.lower() for question in ["types", "programing language"]):
            response = "There is a lot of programing languages but the most common ones are python,java,c++"
        elif all(question in user_input.lower() for question in ["limitations", "bohr's model"]):
            response = """It could not explain the ability of atoms to form molecules by chemical bonds,
Bohr’s theory was also unable to explain the splitting of spectral lines in the presence of magnetic field .
        """
        elif any(question in user_input.lower() for question in ["metamerism"]):
            response = "It is the body segmentation of animals"
        elif any(question in user_input.lower() for question in ["molarity"]):
            response = "It is defined as the number of moles of the solute in 1 litre of the solution"
        elif any(question in user_input.lower() for question in ["molality"]):
            response = "It is defined as the number of moles of solute present in 1 kg of solvent."
        elif any(question in user_input.lower() for question in ["segmentation of body is observed in"]):
            response = "Platyhelminthes"
        elif all(question in user_input.lower() for question in ["what", "software"]):
            response = "The programs and other operating information used by a computer is called software."
        elif all(question in user_input.lower() for question in ["state", "newtons", "second law"]):
            response = "The rate of change of momentum of a body is directly proportional to the applied force and takes place in the direction in which the force acts."
        elif all(question in user_input.lower() for question in ["state", "newtons", "third law"]):
            response = "To every action, there is always an equal and opposite reaction"
        elif all(question in user_input.lower() for question in ["help", "with", "studies"]):
            response = """Yes, I can help you with your studies. You can ask me anything, and I will try to answer as much as possible.
However, if some questions seem unfamiliar to me, I will redirect you to a web browser where you can clear your doubts!"
"""
        elif all(question in user_input.lower() for question in ["made", "you"]):
            response = "I was made by TEAM REDOX"
        elif "cbse" in user_input.lower():
            self.open_web_page("https://www.cbse.gov.in/")
            response = "I've opened a web page for you!"
        elif "google" in user_input.lower():
            self.open_web_page("https://www.google.com/")
            response = "I've opened a web page for you!"
        elif "ncert" in user_input.lower():
            self.open_web_page("https://ncert.nic.in/")
            response = "I've opened a web page for you!"
        elif "youtube" in user_input.lower():
            self.open_web_page("https://www.youtube.com/")
            response = "I've opened a web page for you!"
        elif "spotify" in user_input.lower():
            self.open_web_page("https://open.spotify.com/")
            response = "I've opened a web page for you!"
        elif "english" in user_input.lower():
            self.open_web_page("https://www.youtube.com/watch?v=gCNeDWCI0vo&pp=ygURZW5nbGlzaCBuZXdzIGxpdmU%3D")
            response = "I've opened a web page for you!"
        elif "news" in user_input.lower():
            self.open_web_page("https://www.youtube.com/watch?v=tgBTspqA5nY&pp=ygUTbmV3cyBtYWxheWFsYW0gbGl2ZQ%3D%3D")
            response = "I've opened a web page for you!"
        elif "calculate area" in user_input.lower():
            shapes = ["rectangle", "circle", "triangle", "square"]
            for shape in shapes:
                if shape in user_input.lower():
                    values = [float(val) for val in user_input.split() if val.replace('.', '', 1).isdigit()]
                    response = self.calculate_area(shape, values)
                    break
            else:
                response = "Invalid input for calculating area."
        elif "calculate perimeter" in user_input.lower():
            shapes = ["rectangle", "circle", "triangle", "square"]
            for shape in shapes:
                if shape in user_input.lower():
                    values = [float(val) for val in user_input.split() if val.replace('.', '', 1).isdigit()]
                    response = self.calculate_perimeter(shape, values)
                    break
            else:
                response = "Invalid input for calculating perimeter."
        elif any(op in user_input for op in ['+', '-', '*', '/']):
            response = self.perform_arithmetic(user_input)
        else:
            self.perform_google_search(user_input)
            response = "Ouchh, didn't quite get that... I am redirecting you to Google where you can find the answer to your query."

        return response

    def perform_google_search(self, query):
        webbrowser.open("https://www.google.com/search?q=" + query)

    def save_chat_history(self, instance):
        with open("chat_history.txt", "w") as file:
            file.write(self.chat_history)
        print("Chat history saved to 'chat_history.txt'")
        self.label.text = "Chat history saved to 'chat_history.txt'"
        self.chat_history = ""


if __name__ == "__main__":
    app = EducationalChatbotApp()
    app.run()
