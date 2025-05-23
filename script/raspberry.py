import time
import gpiod
import setup

class Raspberry:
    def __init__(self):
        self.logger = setup.get_logger()

        self.record_runs = False
        self.next_question = False
        self.previous_question = False
        self.power_off = False
        self.speak = False

        self.button_start_recording = 26
        self.button_stop_recording = 19
        self.button_previous_question = 13
        self.button_next_question = 6
        self.button_power_off = 5
        self.button_speak = 12

        self.button_pin_numbers = [self.button_start_recording, self.button_stop_recording, self.button_previous_question, self.button_next_question, self.button_power_off, self.button_speak]
        self.number_of_buttons = len(self.button_pin_numbers)

        self.pressed_buttons = [False for _ in range(self.number_of_buttons)]
        self.button_states = [0 for _ in range(self.number_of_buttons)]

        try:
            self.chip = gpiod.Chip('gpiochip0')
        except FileNotFoundError:
            self.logger.error("GPIO chip not found: This system may not be a Raspberry Pi or you didn't run this file as root or you haven't installed the neccessary libraries")
            self.chip = None
            return

        self.lines = []
        for pin in self.button_pin_numbers:
            line = self.chip.get_line(pin)
            line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN, flags=gpiod.LINE_REQ_FLAG_BIAS_PULL_DOWN)
            self.lines.append(line)

    def update_button_states(self):
        if self.chip == None:
            return

        for i in range(self.number_of_buttons):
            self.button_states[i] = self.lines[i].get_value()

        for i in range(self.number_of_buttons):
            if self.button_states[i] == 1 and not self.pressed_buttons[i]:
                self.pressed_buttons[i] = True
            if self.button_states[i] == 0 and self.pressed_buttons[i]:
                self.pressed_buttons[i] = False
                self.update_internal_states(i)

    def update_internal_states(self, i):
        if 0 == i:
            self.logger.info(f"START RECORDING pressed")
            self.record_runs = True
        elif 1 == i:
            self.logger.info(f"STOP RECORDING pressed")
            self.record_runs = False
        elif 2 == i:
            self.logger.info(f"PREVIOUS QUESTION pressed")
            self.previous_question = True
        elif 3 == i:
            self.logger.info(f"NEXT QUESTION pressed")
            self.next_question = True
        elif 4 == i:
            self.logger.info(f"POWER OFF pressed")
            self.power_off = True
        elif 5 == i:
            self.logger.info(f"READ QUESTION pressed")
            self.speak = True

    def should_record_run(self) -> bool:
        return self.record_runs
    def was_next_question_pressed(self) -> bool:
        result = self.next_question
        self.next_question = False
        return result
    def was_previous_question_pressed(self) -> bool:
        result = self.previous_question
        self.previous_question = False
        return result
    def is_power_button_off(self) -> bool:
        return self.power_off
    def was_speak_pressed(self) -> bool:
        result = self.speak
        self.speak = False
        return result
    
    def release(self):
        if self.chip == None:
            return
        
        self.line_power_off.release()
        self.line_next_question.release()
        self.line_previous_question.release()
        self.line_stop_recording.release()
        self.line_start_recording.release()
        self.line_speak.release()
                                

    
if __name__ == '__main__':
    raspberry : Raspberry = Raspberry()

    start_time = time.time()
    while time.time() - start_time < 60:
        raspberry.update_button_states()
        time.sleep(0.25)

    raspberry.release()