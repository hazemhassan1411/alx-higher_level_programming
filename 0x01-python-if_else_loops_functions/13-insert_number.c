#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a new node into a sorted singly linked list.
 * @head: The head of the linked list.
 * @number: The number for the new node.
 * 
 * Return: The address of the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node;
	listint_t *previous = NULL;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (*head == NULL (*head)->n >= number) {
		new_node->next = *head;
		*head = new_node;
	} else {
		current = *head;
		while (current != NULL && current->n < number) {
			previous = current;
			current = current->next;
		}
		previous->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}