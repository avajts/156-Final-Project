print("hello world")

import kagglehub

# Download latest version of dataset
path = kagglehub.dataset_download("noamsegal/affectnet-training-data")

print("Path to dataset files:", path)