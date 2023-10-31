#include "lists.h"

/**
 * check_cycle - a function in C that checks,
 * if a singly linked list has a cycle in it.
 * @list: A singly-linked list.
 *
 * Return: Return: 0 if there is no cycle, 1 if there is a cycle.
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *hare;
	listint_t *turtle;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return (0);
}
