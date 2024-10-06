import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
import question_answers

class VocabTriviaGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties (title and initial size)
        self.setWindowTitle("Challenge Your Vocabulary!")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.board = question_answers.VocabINFO(18, 6)

        # Create a QLabel to display text
        self.message_label = QLabel("Welcome to Vocab Trivia!")
        self.definition_label = QLabel("Definition: {}".format(self.board.lucky_definition))
        self.hints_label = QLabel("Root Hints. Select Wisely.")

        layout = QVBoxLayout()

        # Add the message_label to the layout
        layout.addWidget(self.message_label)

        # Add the definition_label to the layout
        layout.addWidget(self.definition_label)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        self.create_buttons()

    def create_buttons(self, clear_existing=True):
        if clear_existing:
            # Remove existing buttons
            layout = self.centralWidget().layout()
            for button in getattr(self, 'choice_buttons', []):
                layout.removeWidget(button)
                button.deleteLater()
            for button in getattr(self, 'root_buttons', []):
                layout.removeWidget(button)
                button.deleteLater()

        choice_button_labels = self.board.choices
        root_button_labels = self.board.root_table

        self.choice_buttons = [QPushButton(label) for label in choice_button_labels]
        self.root_buttons = [QPushButton(label) for label in root_button_labels]

        # Connect the correct button click action
        for button in self.choice_buttons:
            button.clicked.connect(self.button_clicked_action)

        # Add buttons to the layout
        layout = self.centralWidget().layout()
        for button in self.choice_buttons:
            layout.addWidget(button)
        for button in self.root_buttons:
            layout.addWidget(button)
        
        # Add the hints_label to the layout
        layout.addWidget(self.hints_label)

    def button_clicked_action(self):
        clicked_button = self.sender()
        label_text = clicked_button.text()

        if label_text == self.board.lucky_word:
            message = "Correct! Next Question:"
            # Reset the game for the next question
            self.board = question_answers.VocabINFO(18, 6)
            self.definition_label.setText("Definition: {}".format(self.board.lucky_definition))
            self.create_buttons(clear_existing=True)  # Update buttons and delete previous buttons
        else:
            message = "Incorrect. Please Try again."

        # Update the text of the message_label
        self.message_label.setText(message)

def main():
    app = QApplication(sys.argv)
    window = VocabTriviaGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
