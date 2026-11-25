# ===========================================================================================
# Laboratorio de Programación (LPR 5° Año) — E.E.S.T. N° 1 "Eduardo Ader" - Vicente López
# ACTIVIDAD 10 BIS: Simulador de Normativa de Celulares en el Aula (Ley 15.678)
# DOCENTE: Mansilla Muñoz York Elías y Yamil De Jesus Ganduglia
# ESTUDIANTE: Maximo Orue
# ===========================================================================================

def evaluar_uso_celular(autorizacion_docente: bool, emergencia_familiar: bool,
                        otro_motivo: bool = False) -> str:
    """Devuelve el mensaje correspondiente según la Ley 15.678.

    Orden de evaluación (importa):
      1) Autorización explícita del docente con fin pedagógico -> uso permitido.
      2) Emergencia familiar validada por preceptoría -> canalización institucional.
      3) El estudiante argumenta otro motivo (ej.: "me aburro") -> motivo no válido.
      4) Ningún caso anterior -> regla general: celular guardado.
    """
    if autorizacion_docente:
        return "[ACCESO PERMITIDO] El celular solo para estudiar y aprender (fines pedagógicos)."
    elif emergencia_familiar:
        return ("[CANALIZACIÓN INSTITUCIONAL] Gestionar la comunicación urgente "
                "a través de preceptoría y/o dirección.")
    elif otro_motivo:
        return ("[MOTIVO NO VÁLIDO] 'Me aburro' u otras excusas no son una excepción "
                "de la Ley 15.678: el celular debe permanecer guardado.")
    else:
        return "[RESTRICCIÓN LEY 15.678] Tu celular debe permanecer guardado en la mochila."


def main():
    print("==================================================")
    print("=== SISTEMA DE ASESORAMIENTO NORMATIVO ESCOLAR ===")
    print("==================================================\n")

    # Variables de contexto del aula (cambiar a True para probar cada rama)
    autorizacion_docente = False  # True si el docente habilitó la actividad digital
    emergencia_familiar = False   # True si fue validado por preceptoría
    otro_motivo = True            # True si el estudiante alega otro motivo (ej.: "me aburro")

    print(f"Estado de Autorización Docente : {autorizacion_docente}")
    print(f"Estado de Emergencia Validada  : {emergencia_familiar}")
    print(f"Alega otro motivo              : {otro_motivo}\n")

    print(evaluar_uso_celular(autorizacion_docente, emergencia_familiar, otro_motivo))
    print("==================================================")

    print("\n--- CASOS DE PRUEBA ---")
    casos = [(True, False, False), (False, True, False), (False, False, True), (False, False, False)]
    for aut, eme, otro in casos:
        print(f"aut={aut!s:5} | emerg={eme!s:5} | otro={otro!s:5} -> {evaluar_uso_celular(aut, eme, otro)}")


if __name__ == "__main__":
    main()
