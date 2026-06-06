import argparse


def main():
    parser = argparse.ArgumentParser(description="Greeter CLI")
    parser.add_argument("name")
    args = parser.parse_args()
    print(f"Welcome, {args.name}")


if __name__ == "__main__":
    main()
