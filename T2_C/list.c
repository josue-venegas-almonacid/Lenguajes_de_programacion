#include <stdio.h>
#include <stdlib.h>
#include "list.h"


void init(struct lista* a){
      a->actual = NULL;
      a->head = NULL;
      a->tail = NULL;
      a->length = 0;
}

void clear(struct lista* a){
      a->actual = a->head;
      int i;
      for(i = 0; i < a->length; i++){
            struct nodo* sig = a->actual->next;
            if (a->actual->info.tipo == 'l'){
                  clear((lista*)(a->actual->info.contenido));
            }
            free(a->actual->info.contenido);
            free(a->actual);
            a->actual = sig;
      }
      a->actual = NULL;
      a->head = NULL;
      a->tail = NULL;
      a->length = 0;
}

void insert(struct lista* a, int i, dato d){
      if(i == 0){
            struct nodo* temp = (struct nodo*)malloc(sizeof(struct nodo));
            temp->info = d;
            temp->next = a->head;
            a->head = temp;
      }
      else {
            if(i < 0 || a->length < i - 1){
                  printf("Indice fuera de rango\n");
                  return;
            }
            a->actual = a->head;
            int index;
            for(index = 1; index < i; index++){
                  a->actual = a->actual->next;
            }
            struct nodo* temp = (struct nodo*)malloc(sizeof(struct nodo));
            temp->info = d;
            temp->next = a->actual->next;
            if(i == 0)
                  a->head = temp;
            else
                  a->actual->next = temp;
      }
      a->length++;
}

void append(struct lista* a, dato d){
      a->actual = (struct nodo*)malloc(sizeof(struct nodo));
      a->actual->info = d;
      a->actual->next = NULL;
      if(a->length == 0)
            a->head = a->actual;
      if(a->tail == NULL)
            a->tail = a->actual;
      else{
            a->tail->next = a->actual;
            a->tail = a->actual;
      }
      a->length++;
}

void remov(struct lista* a, int i){
      a->actual = a->head;
      int index;
      for(index = 0; index < i; index++){
            a->actual = a->actual->next;
      }
      a->actual->next = a->actual->next->next;
      free(a->actual->next);
      a->length--;
}

int length(struct lista a){
  return a.length;
}

struct dato* at(struct lista* a, int i){
      a->actual = a->head;
      int index;
      for(index = 0; index < i; index++){
            a->actual = a->actual->next;
      }
      return &(a->actual->info);
}
