def main():
    arr = ['zero', 'one', 'two', 'three', 'zero', 'five', 'six', 'seven']
    dict1 = { i : arr[i] for i in range(8) }
    print(dict1)
    dict2 = {}
    for key, value in dict1.items():
        if value not in dict2:
            dict2[value] = key
        else:
            dict2[value] = [dict2[value]]
            dict2[value].append(key)
    # dict2 = { value : key for key, value in dict1.items() }
    print(dict2)

if __name__ == "__main__":
    main()
