import pygame
import pygame.midi
import time

def midi_to_float(value):
    """ Converts MIDI value to floating point value between 0 and 1. """
    return value / 127.0

# Initialize pygame.midi
pygame.init()
pygame.midi.init()

# Default to using the first available MIDI input port
input_id = pygame.midi.get_default_input_id()

# Create a MIDI input
midi_input = pygame.midi.Input(input_id)

try:
    while True:
        if midi_input.poll():
            midi_events = midi_input.read(10)

            # Extract MIDI messages from pygame's MIDI event format
            midi_messages = pygame.midi.midis2events(midi_events, midi_input.device_id)

            for msg in midi_messages:
                # Assuming msg is a Control Change message with status 176
                if msg.status == 176:
                    float_value = midi_to_float(msg.data1)  # data1 is the value of the Control Change
                    print(float_value)

        # Don't max out CPU
        time.sleep(0.01)
finally:
    del midi_input
    pygame.midi.quit()
