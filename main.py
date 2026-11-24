"""Entry for make.fun: Two Days of Quiet Dread.

Writes one original code-review comment, at most 140 characters,
approving a pull request with quiet existential dread, to /output/entry.txt.
"""
import os
ENTRY = "Approved. The code works, the tests pass, and in a hundred years none of this will matter, but the diff is clean."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
