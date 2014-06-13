(in-package :mfl)

(om::defmethod! gestionTransporte (listaNotas threshold)
  (setq list listaNotas)
  (if (= 0 (random threshold))
      (setq list (om::om+ listaNotas (* 100 (random 12))))
    )
  list
  )