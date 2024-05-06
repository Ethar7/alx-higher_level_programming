#include "lists.h"
/**
 * is_palindrome - checks palindrome
 *
 * @head: head
 *
 * Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (palindrome(head, *head));
}

/**
 * palindrome- func to know palindrome
 *
 * @head:
 * @end:
 *
 * Return:
*/
int palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
