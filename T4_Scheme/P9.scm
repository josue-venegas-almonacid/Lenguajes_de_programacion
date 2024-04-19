#lang scheme

(define segm
  (lambda (x y)
    (let segm ( (funcion x) (lista y) (listaV '()) (listaF '()))
      (if (null? lista)
          (append listaV listaF)
          (if (funcion (car lista))
             (segm funcion (cdr lista) (append listaV (list(car lista))) listaF)
             (segm funcion (cdr lista) listaV (append listaF (list(car lista))))
             )
          )
      )
    )
  )