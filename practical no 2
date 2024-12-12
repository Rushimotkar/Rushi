user_input = input("Enter String: ")

def long_len():
    str_list = user_input.split(" ")
    max_length = max(str_list, key=len)
    print("Word with the longest length is:", max_length)
    print("Length of longest word:", len(max_length))

def freq_char():
    c = input("Enter Character for Finding its Frequency in String: ")
    print("Character =", c)
    frequency = user_input.count(c)
    print("Frequency:", frequency)

def str_pali():
    reversed_str = user_input[::-1]
    print("Reversed String:", reversed_str)
    if user_input == reversed_str:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")

def index_substr():
    str_sub = input("Enter Substring for Finding its First Appearance Index: ")
    try:
        index = user_input.split(" ").index(str_sub)
        print("Substring found at index:", index)
    except ValueError:
        print("Substring not found.")

def freq_word():
    str_list = user_input.split(" ")
    print("****Count of each word in String*****")
    for word in set(str_list):
        print(f"{word}: {str_list.count(word)}")

if __name__ == '__main__':
    print("*****Take Input*****")
    while True:
        print("1. To Display Word with the Longest Length")
        print("2. To Determine the Frequency of Occurrence of a Character")
        print("3. To Check if String is Palindrome")
        print("4. To Display Index of First Appearance of the Substring")
        print("5. To Count the Occurrence of Each Word in the String")
        print("6. Exit")
        ch = int(input("Enter Your Choice: "))
        
        if ch == 1:
            long_len()
        elif ch == 2:
            freq_char()
        elif ch == 3:
            str_pali()
        elif ch == 4:
            index_substr()
        elif ch == 5:
            freq_word()
        elif ch == 6:
            break
        else:
            print("Invalid choice, please try again.")
