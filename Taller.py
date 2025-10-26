#PARTE 3 DEL TALLER

class Materia:
    def _init_(self, nombre_materia, nota):
        self.nombre_materia = nombre_materia
        self.nota = nota

    def evaluar_nota(self):
        if self.nota < 3:
            return f"{self.nombre_materia}: Pierde ({self.nota})"
        else:
            return f"{self.nombre_materia}: Gana ({self.nota})"


class Estudiante:
    def _init_(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def calcular_promedio(self):
        if not self.materias:
            return 0
        total = sum(m.nota for m in self.materias)
        return total / len(self.materias)

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}")
        for m in self.materias:
            print(m.evaluar_nota())
        print(f"Promedio: {self.calcular_promedio():.2f}")


class SistemaNotas:
    def _init_(self):
        self.lista_estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)

    def mostrar_resultados(self):
        for est in self.lista_estudiantes:
            est.mostrar_info()


# Ejemplo de uso (polimorfismo: distintas materias evalúan con el mismo método)
m1 = Materia("Matemáticas", 4.5)
m2 = Materia("Inglés", 2.8)

est1 = Estudiante("Santiago", 1)
est1.agregar_materia(m1)
est1.agregar_materia(m2)

sistema = SistemaNotas()
sistema.agregar_estudiante(est1)
sistema.mostrar_resultados()


#PARTE 4 DEL TALLER EN JAVA( NO TENGO JAVA )

"""// --------------------------------------------
// PARTE 4 — IMPLEMENTACIÓN EN JAVA
// Mini proyecto: Sistema de Notas
// Autor: (Tu nombre)
// --------------------------------------------

/*
   Descripción general:
   Este programa simula un sistema de notas donde los estudiantes tienen materias
   con calificaciones entre 0 y 5. Si la nota es menor de 3, pierde; si es mayor o igual a 3, gana.
   Se aplica herencia (Persona → Estudiante) y polimorfismo (método mostrarInfo redefinido).
*/

// --------------------------------------------
// CLASE BASE: Persona
// --------------------------------------------
class Persona {
    // Atributos comunes para cualquier persona
    String nombre;
    int id;

    // Constructor que inicializa los atributos
    Persona(String nombre, int id) {
        this.nombre = nombre;
        this.id = id;
    }

    // Método que muestra la información general de la persona
    void mostrarInfo() {
        System.out.println("Nombre: " + nombre + " | ID: " + id);
    }
}

// --------------------------------------------
// CLASE HIJA: Estudiante (hereda de Persona)
// --------------------------------------------
class Estudiante extends Persona {
    // Atributos específicos del estudiante
    Materia[] materias; // Arreglo de materias
    int contador;       // Controla cuántas materias tiene

    // Constructor que usa super() para heredar de Persona
    Estudiante(String nombre, int id, int cantidadMaterias) {
        super(nombre, id); // Llama al constructor de la clase Persona
        materias = new Materia[cantidadMaterias];
        contador = 0;
    }

    // Método para agregar una materia al arreglo
    void agregarMateria(Materia materia) {
        if (contador < materias.length) {
            materias[contador] = materia;
            contador++;
        }
    }

    // Método que calcula el promedio de todas las notas
    double calcularPromedio() {
        double total = 0;
        for (int i = 0; i < contador; i++) {
            total += materias[i].nota;
        }
        return total / contador;
    }

    // Polimorfismo: este método sobreescribe mostrarInfo() de Persona
    @Override
    void mostrarInfo() {
        System.out.println("Estudiante: " + nombre + " (ID: " + id + ")");
        for (int i = 0; i < contador; i++) {
            System.out.println(materias[i].evaluarNota());
        }
        System.out.println("Promedio: " + calcularPromedio());
    }
}

// --------------------------------------------
// CLASE: Materia
// --------------------------------------------
class Materia {
    // Atributos de la materia
    String nombreMateria;
    double nota;

    // Constructor que inicializa los valores
    Materia(String nombreMateria, double nota) {
        this.nombreMateria = nombreMateria;
        this.nota = nota;
    }

    // Método que evalúa si el estudiante gana o pierde la materia
    String evaluarNota() {
        if (nota < 3) {
            return nombreMateria + ": Pierde (" + nota + ")";
        } else {
            return nombreMateria + ": Gana (" + nota + ")";
        }
    }
}

// --------------------------------------------
// CLASE PRINCIPAL: SistemaNotas
// --------------------------------------------
public class SistemaNotas {
    public static void main(String[] args) {

        // Crear dos materias con sus notas
        Materia m1 = new Materia("Matemáticas", 4.5);
        Materia m2 = new Materia("Inglés", 2.8);

        // Crear un estudiante (hereda de Persona)
        Estudiante est1 = new Estudiante("Santiago", 1, 2);

        // Agregar las materias al estudiante
        est1.agregarMateria(m1);
        est1.agregarMateria(m2);

        // Ejemplo de polimorfismo:
        // El objeto persona1 es del tipo Persona, pero apunta a un Estudiante.
        // Al ejecutar mostrarInfo(), usa la versión del Estudiante.
        Persona persona1 = est1;
        persona1.mostrarInfo(); // Se llama el método sobreescrito
    }
}

/*
--------------------------------------------
SALIDA ESPERADA:
--------------------------------------------
Estudiante: Santiago (ID: 1)
Matemáticas: Gana (4.5)
Inglés: Pierde (2.8)
Promedio: 3.65
--------------------------------------------
*/"""