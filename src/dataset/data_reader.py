from mnelab.io.xdf import read_raw_xdf
from pyxdf import resolve_streams, match_streaminfos
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.style import Style

console = Console()

class XDFDataReader:
    def __init__(self, filepath, sub_id='01', ses_id='01'):
        console.print(Panel(f"[bold yellow]Initializing XDFDataReader Class[/bold yellow]", expand=False))
        console.print(f"👤 [bold cyan]Subject:[/bold cyan] {sub_id} | 🗂 [bold cyan]Session:[/bold cyan] {ses_id}")
        
        self.xdf_filepath = filepath
        self.sub_id = sub_id
        self.ses_id = ses_id
        
        console.print("📡 [bold magenta]Resolving streams from XDF file...[/bold magenta]")
        self.streams = resolve_streams(self.xdf_filepath)
        
        self.read_xdf_file()

    def _load_eeg_stream(self):
        console.print("🧠 [bold blue]Loading EEG Data...[/bold blue]")
        eeg_stream_id = match_streaminfos(self.streams, [{'type': 'EEG'}])[0]
        self.eeg = read_raw_xdf(self.xdf_filepath, stream_ids=[eeg_stream_id])
        console.print("✅ [bold green]EEG Data Loaded Successfully![/bold green]")

    def _load_audio_stream(self):
        console.print("🎧 [bold yellow]Loading Audio Data...[/bold yellow]")
        audio_stream_id = match_streaminfos(self.streams, [{'type': 'Audio'}])[0]
        self.audio = read_raw_xdf(self.xdf_filepath, stream_ids=[audio_stream_id])
        console.print("✅ [bold green]Audio Data Loaded Successfully![/bold green]")

    def read_xdf_file(self):
        console.print("📂 [bold magenta]Reading XDF File...[/bold magenta]")
        self._load_eeg_stream()
        #self._load_audio_stream()  # Fixed: Added parentheses to call the function

