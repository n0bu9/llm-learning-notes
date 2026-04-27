import json


if __name__ == "__main__":
    with open("test.json", "r") as f:
        data = json.load(f)
        print(data)
        print(type(data))
