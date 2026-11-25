
# Ley 15.678 — Simulador de uso de celulares en el aula

**Laboratorio de Programación · 5.º año 3.ª (Grupos A-B) · E.E.S.T. N.º 1 «Eduardo Ader», Vicente López**
**Docente:** Mansilla Muñoz York Elías
**Estudiante:** [Apellido y Nombre]
**Actividad 10:** Conciencia digital, algoritmos y marco legal (2.º cuatrimestre, 2026)

## Descripción

Script en Python que simula cómo se decide si un estudiante puede usar el celular en el aula, según la
[Ley 15.678](https://normas.gba.gob.ar/documentos/0QeEmvi4.html) de la Provincia de Buenos Aires. La ley
modifica los artículos 1.º y 3.º de la Ley 15.534: el uso responsable consiste en no utilizar dispositivos
digitales durante la jornada educativa, salvo requerimiento o autorización explícita del docente.

## Lógica de decisión

Las condiciones se evalúan en este orden (el orden importa):

| # | Condición | Resultado |
|---|-----------|-----------|
| 1 | El docente dio autorización explícita con fin pedagógico | Uso permitido como herramienta de estudio |
| 2 | Emergencia familiar real validada por preceptoría | No se usa en el aula; se canaliza por preceptoría y/o dirección |
| 3 | El estudiante alega otro motivo (ej.: «me aburro») | Motivo no válido; el celular permanece guardado |
| 4 | Ningún caso anterior | Regla general: celular guardado en la mochila |

## Estructura del repositorio

```
ley15678/
├── src/
│   └── ley_celulares.py      # Script principal
├── docs/
│   ├── diagrama_flujo.png    # Diagrama de flujo
│   └── InformeEEST1_LPR2026_ACT10_Ley_Apellido_v1.0.0.pdf   # Informe APA v7
├── capturas/                 # Capturas de la ejecución
├── .gitignore
├── LICENSE
└── README.md
```

## Requisitos

- Python 3.8 o superior (no requiere librerías externas)
- Editor sugerido: Visual Studio Code

## Cómo ejecutarlo

```bash
git clone https://github.com/<tu-usuario>/ley15678.git
cd ley15678
python src/ley_celulares.py
```

Para probar cada rama, cambiá los valores de `autorizacion_docente`, `emergencia_familiar` y
`otro_motivo` en la función `main()`. El script también imprime cuatro casos de prueba, uno por rama.

## Ejemplo de salida

```
[MOTIVO NO VÁLIDO] 'Me aburro' u otras excusas no son una excepción de la Ley 15.678: el celular debe permanecer guardado.
```

## Referencias

- Legislatura de la Provincia de Buenos Aires. (2026). *Ley 15.678*. https://normas.gba.gob.ar/documentos/0QeEmvi4.html
- Python Software Foundation. (s. f.). *Más herramientas para control de flujo*. https://docs.python.org/es/3/tutorial/controlflow.html

## Licencia

Distribuido bajo la licencia MIT. Ver [`LICENSE`](LICENSE).

