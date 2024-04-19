#lang scheme

(define ultimo
  (lambda (lista ls)
         (let ult((L lista)(i ls))
           (if (= i 0) (car L) (ult (cdr L) (- i 1))))))

(define largo
  (lambda (lista)
    (let len((i 0)(L lista))
      (if (null? L) i (len (+ i 1) (cdr L))))))

(define minimizar
  (lambda (proc ls)
    (let mini((i 0)(j 1)(menor +inf.0)(L '()))
      (if (or (null? ls)(= (largo ls) 1)) L
          (if (= i j) (if (= (+ j 1) (largo ls)) (if (= (+ i 1) (largo ls)) L (mini (+ i 1) 0 menor L)) (mini i (+ j 1) menor L))         
              (if (< (proc (ultimo ls i) (ultimo ls j)) menor)
                  (if (= (+ j 1) (largo ls)) (mini (+ i 1) 0 (proc (ultimo ls i) (ultimo ls j)) (list (ultimo ls i) (ultimo ls j)))
                      (mini i (+ j 1) (proc (ultimo ls i) (ultimo ls j)) (list (ultimo ls i) (ultimo ls j))))
                  (if (= (+ j 1) (largo ls)) (mini (+ i 1) 0 menor L) (mini i (+ j 1) menor L))))))))


; Casos de prueba no exhaustivos
; Deberían todos retornar #t
(or
 (equal? (minimizar (lambda (x y) (+ x y)) '(4 1 9 2 3)) '(1 2))
 (equal? (minimizar (lambda (x y) (+ x y)) '(4 1 9 2 3)) '(2 1))
)

(equal? (minimizar (lambda (x y) (- x y)) '(4 2 9 3 1)) '(1 9))

(or
 (equal? (minimizar (lambda (x y) (* x y)) '(-4 2 -9 3 1 -5 9)) '(-9 9))
 (equal? (minimizar (lambda (x y) (* x y)) '(-4 2 -9 3 1 -5 9)) '(9 -9))
)

(or
 (equal? (minimizar (lambda (x y) (modulo x y)) '(6 2 3 4)) '(6 3))
 (equal? (minimizar (lambda (x y) (modulo x y)) '(6 2 3 4)) '(6 2))
 (equal? (minimizar (lambda (x y) (modulo x y)) '(6 2 3 4)) '(4 2))
)

(equal? (minimizar (lambda (x y) (/ x y)) '(5 4 3 2 1)) '(1 5))