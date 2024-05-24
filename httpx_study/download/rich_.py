# from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
# import time

# with Progress(TextColumn("[progress.description]{task.description}"),
#               BarColumn(),
#               TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
#               TimeRemainingColumn(),
#               TimeElapsedColumn()) as progress:
#     epoch_tqdm = progress.add_task(description="epoch progress", total=10)
#     batch_tqdm = progress.add_task(description="batch progress", total=100)
#     for ep in range(10):
#         for batch in range(100):
#             print("ep: {} batch: {}".format(ep, batch))
#             progress.advance(batch_tqdm, advance=1)
#             time.sleep(0.1)
#         progress.advance(epoch_tqdm, advance=1)
#         progress.reset(batch_tqdm)
        
        
import tempfile
import httpx
import rich.progress

with tempfile.NamedTemporaryFile() as download_file:
    url = "http://s3.s.cosmoplat.com:8001/model-file-bucket-simulation/5696175f-c7cd-4adf-b90c-421f1f01f63e/pakchunk3946-Windows-1712802409127-3946.pak"
    with httpx.stream("GET", url) as response:
        total = int(response.headers["Content-Length"])

        with rich.progress.Progress(
            "[progress.percentage]{task.percentage:>3.0f}%",
            rich.progress.BarColumn(bar_width=None),
            rich.progress.DownloadColumn(),
            rich.progress.TransferSpeedColumn(),
        ) as progress:
            download_task = progress.add_task("Download", total=total)
            for chunk in response.iter_bytes():
                download_file.write(chunk)
                progress.update(download_task, completed=response.num_bytes_downloaded)