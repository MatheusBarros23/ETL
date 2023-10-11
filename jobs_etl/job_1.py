import kaggle

df = "nelgiriyewithana/world-stock-prices-daily-updating"
dest_path = "./raw_data"
kaggle.api.dataset_download_files(df, path=dest_path, unzip=True)