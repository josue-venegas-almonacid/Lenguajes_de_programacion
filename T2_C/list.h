struct dato {
      void * contenido;
      char tipo;
};

struct nodo {
      struct dato info;
      struct nodo * next;
};

struct lista {
      struct nodo * actual;
      struct nodo * head;
      struct nodo * tail;
      int length;
};

typedef struct lista lista;
typedef struct nodo nodo;
typedef struct dato dato;


void init(struct lista* a);
void clear(struct lista* a);
void insert(struct lista* a, int i, dato d);
void append(struct lista* a, dato d);
void remov(struct lista* a, int i);
int length(struct lista a);
dato* at(struct lista* a, int i);
