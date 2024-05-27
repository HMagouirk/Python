def decode(message_file):
    decoded_message = ""
    with open(message_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                number = int(line)
                with open('C:/Users/Heather/Documents/python/list.txt', 'r') as list_file:
                    for list_line in list_file:
                        list_number, word = list_line.strip().split(' ', 1)
                        if int(list_number) == number:
                            decoded_message += word + " "
                            break

    # Remove the trailing space
    decoded_message = decoded_message.strip()

    return decoded_message

def main():
    message_file = 'C:/Users/Heather/Documents/python/message_file.txt'  # Update this line with the full path
    decoded_message = decode(message_file)
    print(decoded_message)

if __name__ == "__main__":
    main()