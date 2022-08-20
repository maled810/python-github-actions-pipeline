"""A simple GUI calculator"""

import ast
import numpy as np # just to show that 3rd party packages can be installed
from tkinter import Tk, StringVar, Button,Entry
from typing import Union

from calculator.helper import logger
from calculator.settings import (BACKGROUND_COLOR, BUTTON_BG, BUTTON_FG, BUTTON_HEIGHT, BUTTON_WIDTH, CALCULATOR_SIZE,
CALCULATOR_TITLE, ENTRY_IPADX, ENTRY_IPADY)


class GUICalculator:
    """This class implements a simple GUI calculator. """


    def __init__(self) -> None:
        logger.info('Started GUI calculator.')

        self.expression = ''
        gui = Tk()
        gui.configure(background=BACKGROUND_COLOR)
        gui.title(CALCULATOR_TITLE)
        gui.geometry(CALCULATOR_SIZE)

        self.calculation_text = StringVar()
        self.calculation_field = Entry(gui, textvariable=self.calculation_text)
        self.calculation_field.grid(columnspan=4, rowspan=1, ipadx=ENTRY_IPADX, ipady = ENTRY_IPADY)

        button1 = Button(gui, text=' 1 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(1), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button1.grid(row=2, column=0)

        button2 = Button(gui, text=' 2 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(2), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button2.grid(row=2, column=1)

        button3 = Button(gui, text=' 3 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(3), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button3.grid(row=2, column=2)

        button4 = Button(gui, text=' 4 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(4), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button4.grid(row=3, column=0)

        button5 = Button(gui, text=' 5 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(5), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button5.grid(row=3, column=1)

        button6 = Button(gui, text=' 6 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(6), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button6.grid(row=3, column=2)

        button7 = Button(gui, text=' 7 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(7), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button7.grid(row=4, column=0)

        button8 = Button(gui, text=' 8 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(8), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button8.grid(row=4, column=1)

        button9 = Button(gui, text=' 9 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(9), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button9.grid(row=4, column=2)

        button0 = Button(gui, text=' 0 ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button(0), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        button0.grid(row=5, column=0)

        plus = Button(gui, text=' + ', fg=BUTTON_FG, bg=BUTTON_BG,
                    command=lambda: self._press_button('+'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        plus.grid(row=2, column=3)

        minus = Button(gui, text=' - ', fg=BUTTON_FG, bg=BUTTON_BG,
                    command=lambda: self._press_button('-'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        minus.grid(row=3, column=3)

        multiply = Button(gui, text=' * ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button('*'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        multiply.grid(row=4, column=3)

        divide = Button(gui, text=' / ', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button('/'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        divide.grid(row=5, column=3)

        equal = Button(gui, text=' = ', fg=BUTTON_FG, bg=BUTTON_BG,
                    command=self._evalute_expression, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        equal.grid(row=5, column=2)

        clear = Button(gui, text='Clear', fg=BUTTON_FG, bg=BUTTON_BG,
                    command=self._clear_screen, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        clear.grid(row=5, column='1')

        Decimal= Button(gui, text='.', fg=BUTTON_FG, bg=BUTTON_BG,
                        command=lambda: self._press_button('.'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        Decimal.grid(row=6, column=0)

        gui.mainloop()


    def _press_button(self, num: Union[list, bool]) -> None:
        """Method to update the expression"""
        self.expression = self.expression + str(num)
        self.calculation_text.set(self.expression)


    def _evalute_expression(self) -> None:
        """Method to evaluate the expression"""
        try:
            # Normally eval() is unsafe to use with user input, but since in this application there is predefined input, there is no maliciious input
            total = str(eval(self.expression))
            self.calculation_text.set(total)
            self.expression = ''
        except (ValueError, SyntaxError) as e:
            logger.error(f'Error when evaluating expression. Error is: {e}')
            self.calculation_text.set(' Error! ')
            self.expression = ''


    def _clear_screen(self) -> None:
        """This method clears the screen"""
        self.expression = ''
        self.calculation_text.set('')


if __name__ == "__main__":
    calc = GUICalculator()
