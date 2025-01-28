
from mnelab.io.xdf import read_raw_xdf
from pyxdf import resolve_streams, match_streaminfos


from src.utils.graphics import print_section_header

import concurrent.futures
import time
import threading

class XDFDataReader:
    def __init__(self, filepath, sub_id='01', ses_id='01'):
        print_section_header(f'Initializing XDFDataReader Class')
        print(f'Subject: {sub_id} ::: Session: {ses_id}')
        self.xdf_filepath = filepath
        self.sub_id = sub_id
        self.ses_id = ses_id
        self.read_xdf_file()

    def _load_stream(self, stream_type):
        streams = resolve_streams(self.xdf_filepath)
        stream_id = match_streaminfos(streams, [{'type': stream_type}])[0]
        return read_raw_xdf(self.xdf_filepath, stream_ids=[stream_id])

    def _timer(self, stop_event):
        start_time = time.time()
        while not stop_event.is_set():
            elapsed_time = time.time() - start_time
            print(f"\rLoading time elapsed: {elapsed_time:.2f} seconds", end="")
            time.sleep(0.1)  # Update every 100 ms
        print(f"\rLoading complete in {time.time() - start_time:.2f} seconds!")

    def read_xdf_file(self):
        print('Loading the raw data...')
        stop_event = threading.Event()  # Event to signal the timer to stop

        # Start the live timer in a separate thread
        timer_thread = threading.Thread(target=self._timer, args=(stop_event,))
        timer_thread.start()

        try:
            # Parallelize the loading of streams
            with concurrent.futures.ThreadPoolExecutor() as executor:
                eeg_future = executor.submit(self._load_stream, 'EEG')
                audio_future = executor.submit(self._load_stream, 'Audio')

                self.eeg_data = eeg_future.result()
                self.audio_data = audio_future.result()
        finally:
            stop_event.set()  # Signal the timer to stop
            timer_thread.join()  # Wait for the timer thread to finish
