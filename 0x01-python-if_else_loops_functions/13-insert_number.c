#include "lists.h"
#include <stdlib.h> 

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: the number to be inserted
 * 
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;
	listint_t *previous = NULL;

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	new_node->next = current;

	if (previous != NULL)
	{
		previous->next = new_node;
	}

	return (new_node);
}