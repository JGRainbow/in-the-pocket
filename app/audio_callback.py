import argparse
import queue
from datetime import datetime
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
DOWNSAMPLE = 20
WINDOW = 200 # Visible time slot in ms
BATCH_INTERVAL = 1 # In seconds
mapping = [c - 1 for c in CHANNELS]


def input_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    # Fancy indexing with mapping creates a (necessary!) copy:
    audio_queue.put(indata[::DOWNSAMPLE, mapping])


def process_batch(data: np.ndarray):
    print(f'{len(data)} samples created; max value: {data.max()}')
    return data


def create_batch(audio_queue: Queue, duration_seconds: float):
    print(f"Creating {duration_seconds}-second batch from {datetime.utcnow()}")
    time.sleep(duration_seconds)
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
        while True:
            data = create_batch(audio_queue, duration_seconds=BATCH_INTERVAL)
            processed_data = process_batch(data)
            print(audio_queue.qsize())


except Exception as e:
    print(e)
    sys.exit()
    