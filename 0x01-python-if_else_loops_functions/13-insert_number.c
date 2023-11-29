#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - function inserts a new node at a given position
 * @head: pointer to head
 * @number: value of new node
 *
 * Return: Pointer to the new node, NULL otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	int pos = 6;
	listint_t *ptr, *new;

	ptr = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	pos -= 2;

	while (pos)
	{
		ptr = ptr->next;
		pos--;
	}
	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
