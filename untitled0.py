# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pB4pEwoa7v2PG_5gRbyWmLotuMw8Sag4
"""

class cliente:
  def __init__(self,nombre,no_habitacion):
    self.nombre = nombre
    self.no_habitacion = no_habitacion

class node:
  def __init__(self,cliente = None,next= None):
    self.cliente = cliente
    self.next = next

class linked_list:
  def __init__(self):
    self.head = None

  def insertar(self, cliente):
    if not self.head:
      self.head = node(cliente=cliente)
      return
    current=self.head
    while current.next:
      current = current.next
    current.next = node(cliente=cliente)
  
  def imprimir(self):
    node = self.head
    while node != None:
      print(node.cliente.nombre, end = "=>")
      node = node.next
  def eliminar(self, no_habitacion):
    current = self.head
    previous = None

    while current and current.cliente.no_habitacion != no_habitacion:
      previous = current
      current = current.next
    if previous is None:
      self.head = current.next
    elif current:
      previous.next = current.next
      current.next = None

c1 = cliente ("Zapeta",101)
c2 = cliente ("Lopez",103)
c3 = cliente ("Armas",204)
c4 = cliente ("Olmos",302)

lista = linked_list()
lista.insertar(c1)
lista.insertar(c2)
lista.insertar(c3)
lista.insertar(c4)

lista.imprimir()

lista.eliminar(204)

lista.imprimir()

"""## **Listas Circulares**"""

class linked_list_circular:
  def __init__(self,head=None):
    self.head = head
    self.size = 0

  def insertar (self, cliente):
    if self.size ==0:
      self.head = node(cliente = cliente)
      self.head.next = self.head
    else:
      new_node = node(cliente = cliente, next = self.head.next)
      self.head.next = new_node
    self.size += 1
  
  def imprimir(self):
    if self.head is None:
      return
    node = self.head
    print(node.cliente.nombre, end = "=>")
    while node.next != self.head:
      node = node.next
      print(node.cliente.nombre, end = "=>")

  def eliminar(self, no_habitacion):
    node = self.head
    previous = None

    while True:
      if node.cliente.no_habitacion == no_habitacion:
        if previous is not None:
          self.head = node.next
        else:
          while node.next != self.head:
            node = node.next
          node.next = self.head.next
          self.head = self.head.next
        self.size -= 1
        return True
      elif node.next == self.head:
        return False

        previous = node 
        node = node.next

lista_c = linked_list_circular()
lista_c.insertar(c1)
lista_c.insertar(c2)
lista_c.insertar(c3)
lista_c.insertar(c4)

lista_c.imprimir()

lista_c.eliminar(101)

lista_c.imprimir()

"""## **Lista Doblemente enlazada**"""

class node_de:
  def __init__(self, cliente= None, next = None, previous = None):
    self.cliente = cliente
    self.next = next
    self.previous = previous

class linked_list_de:

  def __init__(self, head=None):
    self.head = head
    self.last = head
    self.size = 0

  def insertar(self, cliente):
    if self.size == 0:
      self.head = node_de(cliente=cliente)
      self.last = self.head
    else:
      new_node = node_de(cliente=cliente, next=self.head)
      self.head.previous = new_node
      self.head = new_node
    self.size +=1

  def imprimir (self):
    if self.head is None:
      return
    node = self.head
    print(node.cliente.nombre, end ="=>")
    while node.next:
      node = node.next
      print(node.cliente.nombre, end ="=>")
      
  def eliminar(self, no_habitacion):
      node = self.head
      while node is not None:
        if node.cliente.no_habitacion == no_habitacion:
          if node.previous is not None:
            if node.next:
              node.previous.next = node.next
              node.next.previous = node.previous
            else:
              node.previous.next = None
              self.last = node.previous
          else:
            self.head = node.next
            node.next.previous= self.head
          self.size -=1
          return True
        else:
          node = node.next
      return False

c1 = cliente ("Zapeta",101)
c2 = cliente ("Lopez",103)
c3 = cliente ("Armas",204)

lista_de = linked_list_de()
lista_de.insertar(c1)
lista_de.insertar(c2)
lista_de.insertar(c3)

lista_de.imprimir()