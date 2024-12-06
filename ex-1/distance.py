import re

def main():

    list_1 = []
    list_2 = []

    with open("../input.txt") as fp:
        for line in fp:

        # Testing with first line of input.txt
        # text = "80784   47731"
    
        # Split string, removes whitespace and gives ['80784', '47731'] output
            split_text = str.split(line)
            #print(f"{split_text}")

            list_1.append(split_text[0])
            #print(f"List 1 contents: {list_1}")
            list_2.append(split_text[1])
            #print(f"List 2 contents: {list_2}")

            new_list_1 = list(map(int, list_1))
            new_list_1.sort()
            #print(new_list_1)

            new_list_2 = list(map(int, list_2))
            new_list_2.sort()
            #print(new_list_2)

        distance = sum(abs(new_list_1[i] - new_list_2[i]) for i in range(len(new_list_1)))
        print(f"Total distance between coordinates: {distance}")

main()