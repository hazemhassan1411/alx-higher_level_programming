#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - it is func
 * @list: it is var
 * Return: return
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
					return (1);
	}
	return (0);

}
