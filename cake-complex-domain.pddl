(define (domain cake)
  (:requirements :strips :negative-preconditions) ;comment: this means PDDL1.2
  (:predicates
    (have ?c)
    (eaten ?c)
    (dirty )
  )
  (:action eat
      :parameters (?c)
      :precondition (have ?c)
      :effect (and
          (not (have ?c)) ;"not" means negation
          (eaten ?c)
          (dirty )
      )
  )
  (:action bake
      :parameters (?c)
      :precondition (and (not (have ?c)) (not (dirty)))
      :effect (and (have ?c) (dirty))
  )
  (:action clean
      :parameters ()
      :precondition (dirty)
      :effect (not (dirty))
  )
)