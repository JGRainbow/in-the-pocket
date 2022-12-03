import argparse
import queue
from queue import Queue
import sys
import time

import numpy as np
import sounddevice as sd


def get_device_sample_rate():
    device_info = sd.query_devices(None, 'input')
    return device_info['default_samplerate']


audio_queue = queue.Queue()
DEVICE = None
CHANNELS = [1]
SAMPLERATE = get_device_sample_rate()
DOWNSAMPLE = 5
WINDOW = 200 # Visible time slot in ms
mapping = [c - 1 for c in CHANNELS]


def input_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    # Fancy indexing with mapping creates a (necessary!) copy:
    audio_queue.put(indata[::DOWNSAMPLE, mapping])


def process_batch(data: np.ndarray):
    return data


def create_batch(audio_queue: Queue):
    while True:
        try:
            data = audio_queue.get_nowait()
            return data
        except queue.Empty:
            break


try:
    stream = sd.InputStream(
        device=DEVICE, channels=max(CHANNELS),
        samplerate=SAMPLERATE, callback=input_callback)

    with stream:
        seconds = 0
        while True:
            print(f'Streaming second: {seconds}')
            time.sleep(1)
            seconds += 1
            data = create_batch(audio_queue)
            processed_data = process_batch(data)
            print(f'{len(processed_data)} samples created; max value: {processed_data.max()}')


except Exception as e:
    print(e)
    sys.exit()
    