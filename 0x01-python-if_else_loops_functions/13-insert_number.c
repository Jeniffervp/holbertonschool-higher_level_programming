#include "lists.h"

/**
 * insert_node -  insert a node.
 *@head: is the beginning of the list.
 *@number: index of the node.
 * Return: The numbers of nodes.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *ind;

	ind = *head;
	while (ind->next != NULL && ind->next->n < number)
		ind = ind->next;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (head == NULL)
		return (new);
	if (ind == 0)
	{
		new->next = ind;
		ind = new;
		return (new);
	}
	current = ind;
	while (number < ind->n)
	{
		if (current == NULL)
		{
			free(new);
			return (NULL);
		}
		current = current->next;
		ind--;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
