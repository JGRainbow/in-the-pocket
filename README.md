# In The Pocket

An Application for measuring the swing feel / rhythmic accuracy of two files:

- Master (pre-defined beat pattern / metronome)
- Audio (recorded sample / live audio)

# System Requirements
The I/O is built on top of PyAudio. To install this on your device, refer to [these docs](https://pypi.org/project/PyAudio/).

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