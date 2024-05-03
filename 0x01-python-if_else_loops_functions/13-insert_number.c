#include "lists.h"
#include <stdio.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (!node || newnode->n < node->n)
	{
		newnode->next = node;
		return (*head = newnode);
	}
	while(node)
	{
		if (!node->next || newnode->n < newnode->next->n)
		{
			newnode->next = node->next;
			node->next = newnode;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}			
