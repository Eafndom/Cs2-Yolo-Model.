CS2 Character Detection Model (YOLO)

This model is trained to detect and differentiate between CT- and T-sided player characters in Counter-Strike 2.
Despite CS2 doing its best to make this annoying, the model reliably separates the two teams using visual features alone.

Training Data

Resolution: 1920×1440
Training images: ~1.14k

Despite the relatively small dataset, the model already delivers surprisingly solid CT/T classification performance.

Data Generation

Most images were collected using auto-capture
An older model was used to automatically gather frames
All images were manually reviewed and corrected

That said:
Some labels may still be imperfect — realism beats pretending everything is flawless.
