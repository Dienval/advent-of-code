def main():

    list_1 = []
    list_2 = []

    with open("../input.txt") as fp:
        for line in fp:
    
            split_text = str.split(line)

            list_1.append(split_text[0])
            list_2.append(split_text[1])

            new_list_1 = list(map(int, list_1))
            new_list_2 = list(map(int, list_2))

        sim_score = "1"

main()