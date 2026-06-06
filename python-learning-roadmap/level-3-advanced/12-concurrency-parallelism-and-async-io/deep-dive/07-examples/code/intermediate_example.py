from concurrent.futures import ThreadPoolExecutor

def download(url):
    return f"Downloaded {url}"

urls = ["https://example.com/a", "https://example.com/b"]
with ThreadPoolExecutor() as executor:
    print(list(executor.map(download, urls)))
