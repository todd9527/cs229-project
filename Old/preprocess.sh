# Change this later to take command line arguments

# Converts pdfs to 1 jpg per pg
convert record.pdf record.jpg

python redact_text.py record-*.jpg
