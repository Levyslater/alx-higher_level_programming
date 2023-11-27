#include "lists.h"

/**
 * check_cycle - function checks if singly list is cyclic
 * @list: head pointer
 *
 * Return: 1 if cyclic. 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;

	ptr = list;

	while (ptr != NULL)
	{
		if (ptr->next == list)
			return (1);
		ptr = ptr->next;
	}
	return (0);
}
