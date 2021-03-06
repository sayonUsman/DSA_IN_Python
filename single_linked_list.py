class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data=data, link=self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data=data, link=None)
        temp_node = self.head

        if self.head is None:
            node = Node(data=data, link=None)
            self.head = node

        else:

            while temp_node.link is not None:
                temp_node = temp_node.link

            temp_node.link = node

    def print(self):
        if self.head is None:
            print('\nThe Linked list is Empty.\n')
            return

        else:
            temp_node = self.head

            while temp_node is not None:
                if temp_node.link is None:
                    print(f'{temp_node.data}\n')
                    temp_node = temp_node.link

                else:
                    print(f'{temp_node.data}', end=" -> ")
                    temp_node = temp_node.link


if __name__ == '__main__':
    linked_list = LinkedList()

    while True:
        print('1. Insert at begining.')
        print('2. Insert at end.')
        print('3. Print the Linked List.')
        print('4. Quit.')

        try:
            choice = int(input('\nPlease enter your selected choice: '))

            if choice == 1:
                try:
                    element = int(input('\nPlease enter the element: '))
                    linked_list.insert_at_begining(element)
                    print(
                        f'\n{element} is added at the begining of Linked List Successfully.\n')

                except Exception as error:
                    print(error)
                    print('Try again with INTEGER NUMBER.\n')

            elif choice == 2:
                try:
                    element = int(input('\nPlease enter the element: '))
                    linked_list.insert_at_end(element)
                    print(
                        f'\n{element} is added at the end of Linked List Successfully.\n')

                except Exception as error:
                    print(error)
                    print('Try again with INTEGER NUMBER.\n')

            elif choice == 3:
                linked_list.print()

            elif choice == 4:
                print('\nThe Linked List have closed Successfully.')
                exit()

            else:
                print('\nPlease enter VALID NUMBER only.\n')

        except Exception as error:
            print(error)
            print('Try again with VALID INPUT.\n')
