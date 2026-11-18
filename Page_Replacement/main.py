"""Console page replacement simulator for Platform Technologies."""


def optimal_victim(frames, future_pages):
    """Pick the page whose next use is farthest in the future."""
    victim = frames[0]
    farthest = -1
    for page in frames:
        if page not in future_pages:
            return page  # It will never be needed again.
        next_use = future_pages.index(page)
        if next_use > farthest:
            farthest = next_use
            victim = page
    return victim


def simulate(algorithm, pages, frame_count, show_steps=True):
    """Start with empty frames and return the number of hits and faults."""
    frames = []
    order = []  # FIFO: oldest arrival first. LRU: least recently used first.
    hits = 0
    if show_steps:
        print(f"\n{algorithm} with {frame_count} frame(s)")
        print("Step  Page  Result  Evicted  Frames after request")

    for i, page in enumerate(pages):
        evicted = "-"
        if page in frames:
            result = "Hit"
            hits += 1
            if algorithm == "LRU":
                order.remove(page)
                order.append(page)  # It was just used. FIFO ignores hits.
        else:
            result = "Fault"
            if len(frames) < frame_count:
                frames.append(page)  # A free frame needs no eviction.
            else:
                if algorithm == "Optimal":
                    evicted = optimal_victim(frames, pages[i + 1:])
                else:
                    evicted = order.pop(0)
                frames[frames.index(evicted)] = page
            if algorithm != "Optimal":
                order.append(page)

        if show_steps:
            print(f"{i + 1:>4}  {page:>4}  {result:<6}  {evicted:>7}  {frames}")

    return hits, len(pages) - hits


def read_input():
    while True:
        try:
            frame_count = int(input("Number of frames: "))
            if frame_count > 0:
                break
        except ValueError:
            pass
        print("Enter a whole number of frames greater than zero.")

    while True:
        text = input("Page sequence (example: 1 2 1 3 2): ")
        try:
            pages = [int(word) for word in text.replace(",", " ").split()]
            if pages and all(page >= 0 for page in pages):
                return frame_count, pages
        except ValueError:
            pass
        print("Enter at least one nonnegative page number. Use spaces or commas.")


def main():
    algorithms = {"1": "FIFO", "2": "LRU", "3": "Optimal"}
    frame_count = 3
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    print("Page Replacement Simulator | Platform Technologies")
    print("A sample sequence is loaded. Choose 5 to enter your own.")

    while True:
        print("\nFrame count:", frame_count, "| Page sequence:", *pages)
        print("1. FIFO          2. LRU           3. Optimal")
        print("4. Compare all   5. Change input  0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "0":
            break
        elif choice == "5":
            frame_count, pages = read_input()
        elif choice == "4":
            print("\nAlgorithm  Hits  Faults")
            for name in algorithms.values():
                hits, faults = simulate(name, pages, frame_count, show_steps=False)
                print(f"{name:<9}  {hits:>4}  {faults:>6}")
        elif choice in algorithms:
            hits, faults = simulate(algorithms[choice], pages, frame_count)
            print(f"Page hits: {hits} | Page faults: {faults}")
        else:
            print("Please choose one of the menu numbers (0 to 5).")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting simulator.")
