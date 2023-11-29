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
	listint_t *ptr, *current, *new;

	ptr = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	pos --;

	while (pos)
	{
		current = ptr;
		ptr = ptr->next;
		pos--;
	}
	current->next = new;
	new->next = ptr;

	return (new);
}
