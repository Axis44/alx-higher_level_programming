#include "lists.h"

/**
 * print_dlistint - count number of elements
 * @h: head of list
 *
 * Return: number of elements in list, success
 */
size_t print_dlistint(const dlistint_t *h);
{
	size_t nodes = 0;

	while (h)
	{
		nodes++;
		h = h->next;

	}
	return (nodes);
}
