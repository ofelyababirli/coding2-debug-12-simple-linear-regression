"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "1c8d11f5bb33afff86b7ced00659002a"
GRADE_HASH = "82cc03a228d5eb9111f68438c5776ff96a5035aa58f518ffa3d6e9d24db73a94"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
