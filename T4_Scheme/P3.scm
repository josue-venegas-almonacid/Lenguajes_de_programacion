#lang scheme

(define vs
  (lambda (x)
    (let ((op (car x)) (l1 (second x)) (l2 (third x)))
      (cond
        ((equal? op 'A) (peleaAND l1 l2))
        ((equal? op 'O) (peleaOR l1 l2))
        ((equal? op 'X) (peleaXOR l1 l2))
      ) 
    )
  )
)


;; peleaAND (l1, l2, pares, impares, cont)
;; funcion auxiliar que compara cada elemento. En caso de cumplirse
;; el operador lógico, suma a la respectiva lista 1 punto
;; retorna la lista ganadora, #f en caso de empate

(define peleaAND
  (lambda (x y)
    (let distribuir((l1 x) (l2 y)(pares 0)(impares 0) (cont 1))
      
      ;termina la pelea
      (if (null? l1)
          ;si ganaron los pares, imprime 1, sino 2, empate = #f
          (if (equal? pares impares)
                 #f
                 (if (> pares impares)
                     1
                     2))
      ;peleaAND    
          (if (and (equal? (car l1) 1) (equal? (car l2) 1))
              ;hay puntaje
              (if  (= (modulo cont 2) 0)
                   (distribuir (cdr l1) (cdr l2) (+ pares 1) impares (+ cont 1))
                   (distribuir (cdr l1) (cdr l2) pares (+ impares 1) (+ cont 1)))

              ;no hay puntaje
              (distribuir (cdr l1) (cdr l2) (+ pares 0) (+ impares 0) (+ cont 1))
              )
          )
      )
    )
  )

;; peleaOR (l1, l2, pares, impares, cont)
;; funcion auxiliar que compara cada elemento. En caso de cumplirse
;; el operador lógico, suma a la respectiva lista 1 punto
;; retorna la lista ganadora, #f en caso de empate

(define peleaOR
  (lambda (x y)
    (let distribuir((l1 x) (l2 y)(pares 0)(impares 0) (cont 1))
      
      ;termina la pelea
      (if (null? l1)
          ;si ganaron los pares, imprime 1, sino 2, empate = #f
          (if (equal? pares impares)
                 #f
                 (if (> pares impares)
                     1
                     2))
      ;peleaOR    
          (if (or (equal? (car l1) 1) (equal? (car l2) 1))
              ;hay puntaje
              (if  (= (modulo cont 2) 0)
                   (distribuir (cdr l1) (cdr l2) (+ pares 1) impares (+ cont 1))
                   (distribuir (cdr l1) (cdr l2) pares (+ impares 1) (+ cont 1)))

              ;no hay puntaje
              (distribuir (cdr l1) (cdr l2) (+ pares 0) (+ impares 0) (+ cont 1))
              )
          )
      )
    )
  )

;; peleaXOR (l1, l2, pares, impares, cont)
;; funcion auxiliar que compara cada elemento. En caso de cumplirse
;; el operador lógico, suma a la respectiva lista 1 punto
;; retorna la lista ganadora, #f en caso de empate

(define peleaXOR
  (lambda (x y)
    (let distribuir((l1 x) (l2 y)(pares 0)(impares 0) (cont 1))
      
      ;termina la pelea
      (if (null? l1)
          ;si ganaron los pares, imprime 1, sino 2, empate = #f
          (if (equal? pares impares)
                 #f
                 (if (> pares impares)
                     1
                     2))
      ;peleaXOR    
          (if (xor ((car l1) (car l2)))
              ;hay puntaje
              (if  (= (modulo cont 2) 0)
                   (distribuir (cdr l1) (cdr l2) (+ pares 1) impares (+ cont 1))
                   (distribuir (cdr l1) (cdr l2) pares (+ impares 1) (+ cont 1)))

              ;no hay puntaje
              (distribuir (cdr l1) (cdr l2) (+ pares 0) (+ impares 0) (+ cont 1))
              )
          )
      )
    )
  )


;; xor (x, y)
;; funcion auxiliar que define la operación lógica XOR
;; retorna 1 si (x XOR y) es verdadero. 0 si es falso

(define xor
  (lambda (x y)
    (cond
      ((and (equal? x 0) (equal? y 1)) 1)
      ((and (equal? x 1) (equal? y 0)) 1)
      (else 0))
    )
  )
