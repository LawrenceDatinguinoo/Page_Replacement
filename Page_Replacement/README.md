# Page Replacement Simulator

A console-only Python project for Platform Technologies. Run the same page requests through FIFO, LRU, and Optimal to see which pages stay in memory and how many page faults each policy causes.

## Run it

1. Install Python 3 if needed. No extra packages are required.
2. Open a terminal in the folder containing `main.py`.
3. Run `python main.py`. If your system uses a different command, try `py main.py` on Windows or `python3 main.py` on macOS/Linux.

A sample with **3 frames** is already loaded. Choose **1**, **2**, or **3** for a step-by-step trace, **4** to compare all three totals, **5** to change the frame count and page sequence, or **0** to exit. You can enter pages with spaces (`1 2 1 3 2`) or commas (`1,2,1,3,2`). Every run starts with empty frames.

## Reading the trace

A **frame** holds one page. A **hit** means the requested page is already in a frame. A **fault** means the page must be loaded. A fault uses a free frame if one is available; only a fault with full frames evicts a page. `Evicted` shows `-` when nothing was removed. `Frames after request` lists occupied slots in slot order.

| Policy | When all frames are full, which page leaves? |
| --- | --- |
| FIFO (First In, First Out) | The page that was loaded first. Hits don't change arrival order. |
| LRU (Least Recently Used) | The page that has gone the longest without being requested. |
| Optimal | A page never requested again, or else the page whose next request is farthest away. This needs the future sequence, so it serves as a benchmark. |

## Try it in class

Choose **5**, enter **2** frames and the sequence `1 2 1 3 2`. When page `3` arrives, the frames hold `[1, 2]`. FIFO evicts `1` because it arrived first. LRU evicts `2` because `1` was just used. Optimal evicts `1` because the only remaining request is for `2`.

To check the built-in sample, start the program again and choose **4**. For `7 0 1 2 0 3 0 4 2 3 0 3 2` with 3 frames, the expected totals are:

| Algorithm | Hits | Faults |
| --- | ---: | ---: |
| FIFO | 3 | 10 |
| LRU | 4 | 9 |
| Optimal | 6 | 7 |
