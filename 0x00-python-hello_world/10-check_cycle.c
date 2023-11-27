#include "lists.h"

/**
 * check_cycle - function checks if singly list is cyclic
 * @list: head pointer
 *
 * Return: 1 if cyclic. 0 otherwise
 */

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (1);

	listint_t *ptr;

	ptr = list->next;

	while (ptr != NULL)
	{
		if (ptr == list)
			return (1);
		ptr = ptr->next;
	}
	return (0);
}
