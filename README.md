# Simple Calculator

This project is a basic calculator application built using Python and the Tkinter library for the graphical user interface (GUI). The calculator performs fundamental arithmetic operations, including addition, subtraction, multiplication, and division.

## Screenshots

<p><img src="assets/Screenshot 2024-09-07 223120.png" alt="calculator img"></p>

## Features

- **Addition (+)**
- **Subtraction (-)**
- **Multiplication (*)**
- **Division (/)**
- **Clear function** to reset the input field
- **Equal to (=)** to display the result

## Requirements

- **Python 3.x**
- **Tkinter** (usually comes pre-installed with Python)

## How to Run

1. **Clone** the repository or **copy** the code to your local machine.
2. Run the Python script using the following command:

   ```bash
   python calculator.py
   ```

3. The calculator GUI will open, and you can start using it.

## Code Overview

- The GUI is built using **Tkinter**.
- The calculator features an input field for displaying numbers and results.
- Buttons are created using the `Button` widget and are placed using a grid layout.
- Operations are managed by separate functions handling addition, subtraction, multiplication, and division.
- The `equalto` function calculates the result based on the selected operation and displays it in the input field.

## Example Usage

1. **Input a number** by clicking the numeric buttons.
2. **Choose an operation** (e.g., +, -, *, /).
3. **Input the second number**.
4. **Click =** to see the result.
5. **Click Clear** to reset the calculator for a new calculation.

## Code Snippet

Here is a small code snippet illustrating how the buttons are created and placed in the grid:

```python
button_1 = Button(root, text="1", padx=40, pady=20,background='#2e2e2e',fg='#FFFFFF',command=lambda: button_click(1))
button_1.grid(row=3, column=2)

button_addition = Button(root, text="+", padx=40, pady=20,background='#2e2e2e',fg='#FFFFFF',command=addition)
button_addition.grid(row=4, column=0)
```

## Contributions

Feel free to **fork** this repository and submit **pull requests** if you have improvements or additional features you'd like to add.

## License

This project is open-source and available under the [MIT License](LICENSE).
