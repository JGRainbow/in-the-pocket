import queue
import sys

import numpy as np
import sounddevice as sd


def get_device_sample_rate():
    device_info = sd.query_devices(None, 'input')
    return device_info['default_samplerate']


def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block.
    Assumes single channel for now
    """
    if status:
        print(status, file=sys.stderr)
    # Fancy indexing with mapping creates a (necessary!) copy:
    audio_queue.put(indata[::10, 0])


def process_chunk(audio_queue):
    """
    Process the head of the stream
    """
    global plotdata
    while True:
        try:
            data = audio_queue.get_nowait()
            print(data)
        except queue.Empty:
            break
    #     shift = len(data)
    #     plotdata = np.roll(plotdata, -shift, axis=0)
    #     plotdata[-shift:, :] = data
    # for column, line in enumerate(lines):
    #     line.set_ydata(plotdata[:, column])
    # return lines


if __name__ == '__main__':
    DEVICE = None
    CHANNELS = [1]
    SAMPLERATE = get_device_sample_rate()
    DOWNSAMPLE = 10
    WINDOW = 200 # Visible time slot in ms

    audio_queue = queue.Queue()

    try:
        stream = sd.InputStream(
            device=None, channels=max(CHANNELS),
            samplerate=SAMPLERATE, callback=audio_callback)

        with stream:
            print(audio_queue.get_nowait())

    except Exception as e:
        print(e)

# length = int(WINDOW * SAMPLERATE / (1000 * DOWNSAMPLE))
# plotdata = np.zeros((length, len(CHANNELS)))


# fig, ax = plt.subplots()
# lines = ax.plot(plotdata)
# if len(args.channels) > 1:
#     ax.legend([f'channel {c}' for c in args.channels],
#                 loc='lower left', ncol=len(args.channels))
# ax.axis((0, len(plotdata), -1, 1))
# ax.set_yticks([0])
# ax.yaxis.grid(True)
# ax.tick_params(bottom=False, top=False, labelbottom=False,
#                 right=False, left=False, labelleft=False)
# fig.tight_layout(pad=0)

# stream = sd.InputStream(
#     device=args.device, channels=max(args.channels),
#     samplerate=args.samplerate, callback=audio_callback)
# ani = FuncAnimation(fig, update_plot, interval=args.interval, blit=True)
# with stream:
#     plt.show()
# except Exception as e:
#     parser.exit(type(e).__name__ + ': ' + str(e))