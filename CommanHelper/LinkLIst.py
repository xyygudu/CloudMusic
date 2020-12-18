# -*- coding: utf-8 -*-

"""
Created on 2020/5/13 14:57
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

class Node:
    def __init__(self, item):
        self.item = item  # 该节点值
        self.next = None   # 连接一下一个节点
        self.prev = None  # 上一个节点值


class DoubleCircularLinkedList:
    """双向循环列表类"""
    def __init__(self):
        self._head = None

    @property
    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return not self._head

    @property
    def length(self):
        """
        链表长度
        :return:
        """
        if self.is_empty:
            return 0
        else:
            cur = self._head.next
            n = 1
            while cur != self._head:
                cur = cur.next
                n += 1
            return n

    @property
    def ergodic(self):
        """
        遍历链表
        :return:
        """
        if self.is_empty:
           raise ValueError("ERROR NULL")
        else:
            cur = self._head.next
            print(self._head.item)
            while cur != self._head:
                print(cur.item)
                cur = cur.next

    def add(self, item):
        """
        头部添加节点
        :return:
        """
        node = Node(item)
        if self.is_empty:
            node.next = node
            node.prev = node
            self._head = node
        else:
            node.next = self._head
            node.prev = self._head.prev
            self._head.prev.next = node
            self._head.prev = node
            self._head = node

    def append(self, item):
        """
        尾部添加节点
        :param item:
        :return:
        """
        if self.is_empty:
            self.add(item)
        else:
            node = Node(item)
            cur = self._head.next
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.prev = cur
            node.next = self._head
            self._head.prev = node

    def insert(self, index, item):
        """
        任意位置插入节点
        :param item:
        :return:
        """
        if index == 0:
            self.add(item)
        elif index+1 >= self.length:
            self.append(item)
        else:
            cur = self._head.next
            n = 1
            while cur.next != self._head:
                if n == index:
                    break
                cur = cur.next
                n += 1
            node = Node(item)
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node

    def search(self, item):
        """
        查找节点是否存在
        :return:
        """
        if self.is_empty:
            return False
        else:
            cur = self._head.next
            if self._head.item == item:
                return True
            else:
                while cur != self._head:
                    if cur.item == item:
                        return True
                    else:
                        cur = cur.next
                return False

    def delete(self, item):
        """
        删除指定值的节点
        :param item:
        :return:
        """
        if self.is_empty:
            raise ValueError("ERROR NULL")
        else:
            if self._head.item == item:
                if self.length == 1:
                    self._head = Node
                else:
                    self._head.prev.next = self._head.next
                    self._head.next.prev = self._head.prev
                    self._head = self._head.next
            cur = self._head.next
            while cur != self._head:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                cur = cur.next

    def getHead(self):
        return self._head

if __name__ == '__main__':
    d = DoubleCircularLinkedList()
    d.append(1)
    d.append(2)
    a = d.getHead()
    print(a.item)