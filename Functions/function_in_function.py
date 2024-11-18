def first(name):
    print(f"Hello {name} from first")

    def second():
        print(f"Hello {name} from second")
    second()

first("Yash")