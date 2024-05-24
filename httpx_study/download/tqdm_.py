import tempfile
import httpx
from tqdm import tqdm

with tempfile.NamedTemporaryFile() as download_file:
    url = "http://s3.s.cosmoplat.com:8001/model-file-bucket-simulation/5696175f-c7cd-4adf-b90c-421f1f01f63e/pakchunk3946-Windows-1712802409127-3946.pak"
    with httpx.stream("GET", url) as response:
        total = int(response.headers["Content-Length"])

        with tqdm(total=total, unit_scale=True, unit_divisor=1024, unit="B") as progress:
            num_bytes_downloaded = response.num_bytes_downloaded
            for chunk in response.iter_bytes():
                download_file.write(chunk)
                progress.update(response.num_bytes_downloaded - num_bytes_downloaded)
                num_bytes_downloaded = response.num_bytes_downloaded