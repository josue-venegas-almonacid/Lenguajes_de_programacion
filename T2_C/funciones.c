#include <stdio.h>
#include <stdlib.h>
#include "list.h"
#include "funciones.h"


struct lista* map(struct lista* a, dato (*f)(struct dato)){
      lista *b = (lista*)malloc(sizeof(lista));
      init(b);
      int i;
      a->actual = a->head;
      for(i = 0; i < a->length; i++){
            append(b, f(a->actual->info));
            a->actual = a->actual->next;
      }
      return b;
}

void print_level(int level){
      /*
      Nombre: print_level
      Descripcion: Funcion auxiliar de print. Si el elemento
      actual pertenece a una lista anidada, se imprime con
      un cierto numero de tabulaciones adicionales.
      Inputs:
      (int) level: Representa lo anidado que esta el
      elemento en la lista.
      Outputs:
      Nada, es una funcion void.
      */
      int i;
      for(i = 0; i < level; i++){
            printf("\t");
      }
}
void aux_print(struct lista* a, int level){
      /*
      Nombre: aux_print
      Descripcion: Funcion auxiliar de print. Recorre
      cada elemento de la lista y, segun lo anidado que este,
      agrega tabulaciones con print_level y luego lo imprime.
      Inputs:
      (struct lista* a): Puntero a la lista a imprimir.
      (int) level: Representa lo anidado que esta el elemento
      en la lista.
      Outputs:
      Nada, es una funcion void.
      */
      int i;
      a->actual = a->head;
      printf("\n");
      print_level(level);
      printf("[\n");
      for(i = 0; i < a->length; i++){
            print_level(level);
            printf("(%i): ", i);
            dato data = a->actual->info;
            if(data.tipo == 'l'){
                  aux_print((lista*)data.contenido, level + 1);
            }else{
                  if(data.tipo == 'f'){
                        printf("%f\n", *((float*)data.contenido));
                  }     else  {
                        printf("%i\n", *((int*)data.contenido));
                  }
            }
            a->actual = a->actual->next;
      }
      print_level(level);
      printf("]\n");
}

void print(struct lista* a){
      aux_print(a, 0);
}

float sum(struct lista* a){
      float suma = 0.0;

      a->actual = a->head;
      int index;
      for (index = 0; index < (a->length); index++){
            if (a->actual->info.tipo == 'l'){
                  suma+= sum(a->actual->info.contenido);
            }
            else if (a->actual->info.tipo == 'i'){
                  suma+= *(int*)(a->actual->info.contenido);
            }
            else if (a->actual->info.tipo == 'f'){
                  suma+= *(float*)(a->actual->info.contenido);
            }
            a->actual = a->actual->next;
      }
      return suma;
}

float average(struct lista* a){
      float suma = 0.0;
      float prom = 0.0;
      int listas_vacias = 0;

      a->actual = a->head;
      int index;
      for (index = 0; index < (a->length); index++){
            if (a->actual->info.tipo == 'l'){
                  if ((((lista*)(a->actual->info.contenido))->length) != 0){
                        suma+= average(a->actual->info.contenido);
                  }
                  else {
                        listas_vacias++;
                  }
            }
            else if (a->actual->info.tipo == 'i'){
                  suma+= *(int*)(a->actual->info.contenido);
            }
            else if (a->actual->info.tipo == 'f'){
                  suma+= *(float*)(a->actual->info.contenido);
            }
            a->actual = a->actual->next;
      }

      prom = suma / ((a->length) - listas_vacias);
      return prom;
}
