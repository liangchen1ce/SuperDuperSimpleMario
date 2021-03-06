import pyaudio
import wave
import data


# This is modified from examples in PyAudio official website
def playMusic(choice):
    if choice == "default":
        fileName = "muyu.wav"
        path = data.Data().filePath(fileName)
    else:
        path = choice

    count = 0
    while count < 15:
        count += 1
        wf = wave.open(path, 'rb')

        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # open stream using callback (3)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        datas = wf.readframes(1024)

        while datas != '':
            stream.write(datas)
            datas = wf.readframes(1024)

            # stop strqqeam (6)
        stream.stop_stream()
        stream.close()

        # close PyAudio (7)
        p.terminate()