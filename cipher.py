#!/user/bin/env python3
from enigma.machine import EnigmaMachine


def simpleShift(shift):
    print('test')


'''
Enigma Machine Configuration

Source
https://py-enigma.readthedocs.io/en/latest/guide.html#example-communication-procedure
'''
__enigma_machine = EnigmaMachine.from_key_sheet(
    rotors='II IV V',
    reflector='B',
    ring_settings='B U L',
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')


def enigma_set_key(key):
    # __enigma_machine.set_display('ABC')
    __enigma_machine.set_display(key)  # set initial rotor positions


def enigma_process(plaintext):
    # return __enigma_machine.process_text(plaintext, replace_char='X')
    return __enigma_machine.process_text(plaintext)


if __name__ == '__main__':
    simpleShift()
