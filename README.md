CS2 Character Detection Model (YOLO)

This model is trained to detect player characters in Counter-Strike 2.
It does not differentiate between enemies and teammates, as there is currently no reliable way to do so using YOLO alone (CS2 doesn’t exactly make this easy either).

Training Data

Resolution: 1920×1440

Training images: ~512

Despite the relatively small dataset, the model already delivers surprisingly solid performance

Data Generation

Most images were collected using auto-capture

An older model was used to automatically gather frames

All images were manually reviewed and corrected

That said:
Some labels may still be imperfect — realism beats pretending everything is flawless.

Current Status

Reliable detection of player models

No friend/foe classification (intentional, not an oversight)

Well suited as a base or pre-training model for further improvements
