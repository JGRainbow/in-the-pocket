# In The Pocket

An Application for measuring the swing feel / rhythmic accuracy of two files:

- Master (pre-defined beat pattern / metronome)
- Audio (recorded sample / live audio)

# System Requirements
The I/O is built on top of SoundDevice. To install this on your device, refer to [these docs](https://python-sounddevice.readthedocs.io/en/0.4.5/installation.html).

After that, simply run `poetry install` from the root directory. 

# Output Requirements

- Live information — ‘you’re rushing!’
- End of session report — ‘you’re consistently late on the third quaver’

# Input Requirements

- Maybe a setting for straight / swung
- Live audio input
- Predefined metronome bpm / time signature (for now)

### Future Requirements

- Automatic beat detection
- Automatic swing detection

# Basic Components

- `AudioInput`
- `NoteFilter`
- `QuantisationMetric`
- `ReportCreator`

# Troubleshooting
Refer [here](https://stackoverflow.com/questions/33513522/when-installing-pyaudio-pip-cannot-find-portaudio-h-in-usr-local-include) for any issues installing portaudio.