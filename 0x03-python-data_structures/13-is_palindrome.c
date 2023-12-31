#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - function checks if a list is palindrome
 * @head: pointer to head
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	unsigned int m, start = 0;
	int arr[10265];
	
	current = *head;
	if (current == NULL)
		return (1);
	m = 0;

	while (current != NULL)
	{
		arr[m] = current->n;
		current = current->next;
		m++;
	}
	m -= 1;
	while (start < m)
	{
		if (arr[start] != arr[m])
			return (0);
		start++;
		m--;
	}
	return (1);
}
