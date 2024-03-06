import sys
import question_answers, vocab_trivia
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel

class VocabTriviaGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties (title and initial size)
        self.setWindowTitle("Challenge Your Vocabulary!")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Your code for board initialization and buttons
        self.board = question_answers.VocabINFO(18, 6)
        print(self.board.lucky_word)
        print(self.board.choices)
        print(self.board.lucky_definition)
        print(self.board.root_table)

        choice_button_labels = self.board.choices
        root_button_labels = self.board.root_table

        choice_buttons = [QPushButton(label) for label in choice_button_labels]
        root_buttons = [QPushButton(label) for label in root_button_labels]


        # Create a QLabel to display text
        self.message_label = QLabel("Welcome to Vocab Trivia!")
        self.definition_label = QLabel("Definition: {}".format(self.board.lucky_definition))        
        self.hints_label = QLabel("Root Hints. Select Wisely.")
        layout = QVBoxLayout()

        
        layout.addWidget(self.definition_label)
        for button in choice_buttons:
            layout.addWidget(button)
            button.clicked.connect(self.button_clicked_action)

        layout.addWidget(self.hints_label)
        for button in root_buttons:
            layout.addWidget(button)

        # Add the message_label to the layout
        layout.addWidget(self.message_label)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

    def button_clicked_action(self):
        clicked_button = self.sender()
        label_text = clicked_button.text()

        if label_text == self.board.lucky_word:
            message = "Correct!"
        else:
            message = "Incorrect. Please Try again."

        # Update the text of the message_label
        self.message_label.setText(message)

    #TODO: Index definitions for roots, and write requirements.txt file
def main():
    app = QApplication(sys.argv)
    window = VocabTriviaGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

