from app import send_message
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('name', type=str,
                    help='A required string argument for skype name')

    parser.add_argument('message', type=str,
                    help='A required string argument for message to send')
    args = parser.parse_args()
    print(send_message(args.name,args.message))
