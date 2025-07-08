# utils.py
import os
import shutil
import datetime

# Voorbeeld utility: bestandsbeheer
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Bestand verplaatst van {source} naar {destination}")
    except Exception as e:
        print(f"Fout bij verplaatsen van bestand: {e}")

# Voorbeeld utility: datumformaat
def current_datetime(1):
    now = datetime.datetime.now(1)
    return now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    print(f"Huidige datum en tijd: {current_datetime(1)}")
