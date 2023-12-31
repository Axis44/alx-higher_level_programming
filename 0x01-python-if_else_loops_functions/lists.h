#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 *struct listint_s - singly linked list
 *@n: integer
 *@next: next node point
 *Description: node structure of singly linked list
 *
 */

typedef struct listint_s
{
        int n;
        struct listint_s *next;
} listint_t;


def islower(c);
def uppercase(str);
def print_last_digit(number);
def add(a, b);
def pow(a, b);
void free_listint(listint_t *head);
listint_t *add_nodeint_end(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
