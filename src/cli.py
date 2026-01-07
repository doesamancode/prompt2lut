import argparse
import time
from models import StyleParameters

def main():
    start_time = time.time()

    parser = argparse.ArgumentParser(
        description = "Prompt2LUT - Prompt based LUT generator"
    )

    parser.add_argument(
        "--prompt", "-p",
        required = True,
        type = str,
        help = "Text prompt describing the desired look"
    )

    parser.add_argument(
        "--output", "-o",
        required = True,
        type = str,
        help = "Output .cube LUT file path"
    )

    parser.add_argument(
        "--dry-run",
        action = "store_true",
        help = "Run without writing LUT file"
    )

    args = parser.parse_args()
    
    print("\n=== Prompt2LUT ===\n")
    print("Raw Prompt:")
    print(f"    {args.prompt}\n")

    params = StyleParameters.neutral()

    print("Style Parameters (Neutral Base):")
    print(params)
    
    elapsed = (time.time() - start_time) * 1000
    print(f"Total Time: {elapsed:.2f} ms")

if __name__ == "__main__":
    main()