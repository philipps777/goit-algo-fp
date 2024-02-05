
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def sort_list(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_head

    def merge_sorted_lists(list1, list2):
        new_list = LinkedList()
        current_list1 = list1.head
        current_list2 = list2.head

        while current_list1 is not None and current_list2 is not None:
            if current_list1.data < current_list2.data:
                new_list.insert_at_end(current_list1.data)
                current_list1 = current_list1.next
            else:
                new_list.insert_at_end(current_list2.data)
                current_list2 = current_list2.next

        while current_list1 is not None:
            new_list.insert_at_end(current_list1.data)
            current_list1 = current_list1.next

        while current_list2 is not None:
            new_list.insert_at_end(current_list2.data)
            current_list2 = current_list2.next

        return new_list


def main():
    print("Виконуємо додавання елементів до зв'язного списку:")
    llist = LinkedList()
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    print("Зв'язний список:")
    llist.print_list()

    llist.delete_node(10)
    print("\nЗв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)

    print("\nЗв'язний список після реверсу:")
    llist.reverse_list()
    llist.print_list()

    llist2 = LinkedList()
    llist2.insert_at_end(7)
    llist2.insert_at_end(12)
    llist2.insert_at_end(18)
    print("\nДругий зв'язаний список:")
    llist2.print_list()

    llist.sort_list()
    print("\nВідсортований перший список:")
    llist.print_list()

    merged_list = llist.merge_sorted_lists(llist2)
    print("\nОб'єднаний та відсортований список:")
    merged_list.print_list()


if __name__ == "__main__":
    main()


# Виконуємо додавання елементів до зв'язного списку:
# Зв'язний список:
# 15
# 10
# 5
# 20
# 25

# Зв'язний список після видалення вузла з даними 10:
# 15
# 5
# 20
# 25

# Шукаємо елемент 15:
# 15

# Зв'язний список після реверсу:
# 25
# 20
# 5
# 15

# Другий зв'язаний список:
# 7
# 12
# 18

# Відсортований перший список:
# 5
# 15
# 20
# 25

# Об'єднаний та відсортований список:
# 5
# 7
# 12
# 15
# 18
# 20
# 25
