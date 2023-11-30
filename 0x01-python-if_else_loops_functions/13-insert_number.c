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
	listint_t *ptr;

	if (head == NULL)
		return NULL;
	ptr = malloc(sizeof(listint_t));

	if (ptr == NULL)
		return NULL;
	ptr->n = number;
	ptr->next = NULL;
	return (ptr);
