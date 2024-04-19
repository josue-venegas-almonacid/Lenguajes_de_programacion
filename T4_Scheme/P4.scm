#lang scheme

(define (orden n mat)
  (let ((n n) (mat mat) (contador 0) (orden #t))
    (if (= n 0)
        #f
        (if (or (if (rev-col mat n) #t #f)
                (if (rev-fil mat) #t #f)                
                (if (ord-lista (diag mat)) #t #f))
            #t
            #f
            ))
    )
  ) 


;; (diag) (mat)
;; Funcion auxiliar que retorna una lista con la diagonal de la matriz
;; Retorna la lista
(define diag
  (lambda (mat)
    (cond
      ((null? mat) '())
      (else (cons (car (car mat)) (diag (map cdr (cdr mat))))))
    )
  )

;; (columna) (mat nc)
;; Funcion que retorna una lista con una columna de la matriz
;; Retorna la lista
(define columna
  (lambda (mat nc)
    (cond
      ((null? mat) '())
      (else (cons (list-ref (car mat) nc) (columna (cdr mat) nc)))
          )
    )
  )

;; (rev-col) (mat n)
;; Revisa si la mat esta ordenada por columna
;; Retorna #t si está ordenada por columna, sino retorna #f
(define (rev-col mat n )
  (let revi ((mat mat) (n n) (contador 0))
    (if (< contador n)
        (if (ord-lista (columna mat contador))
            #t
            (revi mat n (+ contador 1))
            )
        #f)
    )
  )

;; (rev-fil) (mat)
;; Revisa si la mat esta ordenada por fila
;; Retorna #t si está ordenada por fila, sino retorna #f
(define rev-fil
  (lambda (mat)
    (cond
      ((null? mat) #f)
      (else (if (ord-lista (car mat)) #t (rev-fil (cdr mat)))))4
    )
  )

;; (ord-lista) (lista)
;; Funcion auxiliar. Verifica uno por uno si la fila esta ordenada
;; Si está ordenada orden = #t, si está desordenada orden = #f
(define (ord-lista lista)
  (let ord-sub((lista (cdr lista)) (minimo (car lista)) (orden #t))
    (cond
      ((> (car lista)  minimo) (set! minimo (car lista)))
      ((< (car lista) minimo) (set! orden #f))
      ((= (car lista) minimo) (set! orden #f))
      )(if (null? (cdr lista)) orden (ord-sub (cdr lista) minimo orden))
    )
  )