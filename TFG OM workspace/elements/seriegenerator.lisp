(setq listaBase '(2 5 0 0 0 0 0 0 0 0 0 0))
(setq minNotas 4)
(setq maxNotas 5)

; function to rotate a list:
; (my-rotate (list 0 1 2 3 4 5)) -> (1 2 3 4 5 0)
; (my-rotate (list 0 1 2 3 4 5) 2) -> (2 3 4 5 0 1)
(defun my-rotate (list &optional (n 1))
(if (<= n 0) list (my-rotate (append (last list) (reverse (cdr (reverse list)))) (1- n))))
; function to randomize a list
(defun randomize-list (list)
(setf temp-list nil)
(dotimes (i (length list))
(setf list (my-rotate list (random (length list))))
(setf temp-list (push (car list) temp-list))
(pop list))
temp-list)




(defun myf (listaB min max)
  
  (setq notas '(1 2 3 4 5 6 7 8 9 10 11 12))
    ; Obtiene las notas que faltan en la secuencia parcial
  (setq notasfaltan (delete nil (remove-duplicates (loop for x in notas
     collect (if (member x listaB) nil x))  ; comprobar si x está en lista y si no está, añadir a notasfaltan
  )))

  (setq notasfaltan (randomize-list notasfaltan)) ; reordenar aleatoriamente notasfaltan

  (loop for x in notasfaltan do     ; para cada elemento de notasfaltan (bucle)
      (setq lista (copy-list listaB)) ;Creamos una copia para no modificar la lista original
      ; seleccionar nueva nota y comprobar si cumple las restricciones
      ; obtener posición del primer 0
      ; en la posición -1 está la nota anterior
      (if (= 0 (position 0 lista)) ; Si es la primera posición de la lista
          (progn
          (setf (nth (position 0 lista) lista) x)
          (if (not (position 0 (myf lista min max))); llama recursivamente a myf con la nueva lista
                                  ; si myf devuelve una lista completa entonces termina y devuelve la lista
              (return (myf lista min max))
            )
          )

          (if (and ; Si no es la primera posición de la lista, miramos las restricciones
              (>= (if (> (abs (- x (nth (- (position 0 lista) 1) lista))) 6)
                  (- 6 (- (abs (- x (nth (- (position 0 lista) 1) lista))) 6))
                  (abs (- x (nth (- (position 0 lista) 1) lista)))) min)
              (<= (if (> (abs (- x (nth (- (position 0 lista) 1) lista))) 6)
                  (- 6 (- (abs (- x (nth (- (position 0 lista) 1) lista))) 6))
                  (abs (- x (nth (- (position 0 lista) 1) lista)))) max)
              )
              (progn
              (setf (nth (position 0 lista) lista) x); si las dos notas cumplen las restricciones, asigna la nueva nota en la posición del primer cero
              (if (not (position nil (myf lista min max))); llama recursivamente a myf con la nueva lista
                                  ; si myf devuelve una lista completa entonces termina y devuelve la lista
                  (return (myf lista min max))
              )
              )
          )
      )
  )
  
  (if (position 0 lista)
      '(nil)
      lista)
  ; si al terminar el bucle ninguna nota cumple la restricción devuelve lista vacía
)