import kagglehub

# Download latest version
path = kagglehub.dataset_download("troubador/2026-world-cup-player-statistics")

print("Path to dataset files:", path)