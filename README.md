# Similar Image Search by Textures
Searching for Similar Image by Textures.

# Usage

## Phase 0: Preparing Dataset
 - Create a folder named `images`
 - Then, put all textures images you want to index in this folder

## Phase 1: Indexing
run the following commande
`python indexing.py`. it will generate a file `histograms.csv` which containe the unique features vector of each image.

## Phase 2: Search
run the following commande
`python matching.py`. then choose the image you're looking for similars.

