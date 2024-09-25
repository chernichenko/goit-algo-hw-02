import queue
import random

request_queue = queue.Queue()

def generate_request():
    new_request = f"Request-{random.randint(1000, 9999)}"
    print(f"Generated: {new_request}")
    request_queue.put(new_request)

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processed: {request}")
    else:
        print("No requests to process. Queue is empty.")

def main():
    while True:
        user_input = input("Press 'g' to generate a request, 'p' to process a request, or 'q' to quit: ")
        if user_input == 'g':
            generate_request()
        elif user_input == 'p':
            process_request()
        elif user_input == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()