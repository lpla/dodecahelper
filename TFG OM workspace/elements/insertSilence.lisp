(defun insert-at (elem org-list pos)
    (if (or (eql pos 1) (eql org-list nil))
            (cons elem org-list)
            (cons (car org-list) (insert-at elem (cdr org-list) (- pos 1)))))



(defun insertarSilencios (listaNotas numeroSilencios)
  (setq list listaNotas)
  (loop for i from 1 to numeroSilencios do
        (setq list (insert-at 0 list (+ 1 (random (length list)))))
        )
  list
  )