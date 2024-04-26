#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check cycle
 *
 * @list: pointer
 *
 * Return: 1 or 0
*/
int check_cycle(listint_t *list)
{
	listint_t *head = list, *tail = list;

	while (tail && tail->next)
	{
		head = head->next;
		tail = tail->next->next;
		if (tail == head)
			return(1);
	}
	return (0);
}
