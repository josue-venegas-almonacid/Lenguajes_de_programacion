/** Atributos agregados:
(Metodo) initialize(Pais): Apertura y lectura de los archivos
(Metodo) getFile(String): Manejo de errores
(Metodo) toInt(String): Transformacion de string a entero
*/

import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.Arrays;
import java.util.HashMap;


class Main
{
    public static void main(String args[])
    {
        // Instanciamos el pais, y registramos la empresa y las ciudades
        Pais pais = new Pais();
        initialize(pais);

        Empresa empresa = pais.getEmpresa();
        Ciudad[] ciudades = pais.getCiudades();
        final int length = ciudades.length;

        // Creamos arreglos para registrar las utilidades y transportes
        int maxId = -1;
        int[] utilidades = new int[length];
        int[] camiones = new int[length];
        int[] camionetas = new int[length];

        // Registramos los ingresos por consumo
        for(int i = 0; i < length; i++){
            Ciudad ciudad = ciudades[i];
            HashMap<Integer, Integer> connections = ciudad.getConnections();

            if(ciudad.getCasas().length > 0){
                camionetas[i] = 1;
                utilidades[i] += ciudad.getConsumoCasas() * empresa.getPrecioBalon();
            }
            if(ciudad.getEdificios().length > 0){
                camiones[i] = ciudad.getEdificios().length;
                utilidades[i] += ciudad.getConsumoEdificios() * empresa.getPrecioLitro();
            }
        }

        // Calculamos las utilidades
        for(int i = 0; i < length; i++){
            int localCamiones = 0;
            int localCamionetas = 0;

            for(int j = 0; j < length; j++){
                if(j != i){
                    localCamiones += camiones[j];
                    localCamionetas += camionetas[j];
                }
            }
            //System.out.println("[" + i + "] Ingresos: " + utilidades[i]);
            //System.out.println("[" + i + "] Camiones|Camionetas: " + localCamiones + " - " + localCamionetas);
            utilidades[i] -= (localCamiones + localCamionetas) * empresa.getPrecioTransporte();
        }

        // Obtenemos la ciudad optima para la empresa
        int id = -1;
        int max = 0;
        for(int i = 0; i < length; i++){
            if(utilidades[i] > max)
                max = utilidades[i];
                id = i;
        }
        System.out.println("La ciudad " + id + " es la ubicación óptima");
        for(int i = 0; i < length; i++){
            System.out.println("Ciudad " + i + ":");
            System.out.println("- Utilidad: " + utilidades[i]);
            System.out.println("- Se utilizaron " + camiones[i] + " camiones cisternas y " + camionetas[i] + " camionetas");
        }
        return;
    }

    /** (initialize)
    (Pais) (pais)
    -------------------------
    Método para leer los archivos y crear los datos necesarios para la solucion del problema
    -------------------------
    */
    private static void initialize(Pais pais){
        // Lectura del mapa
        //System.out.println("Leyendo 'mapa.txt'");
        Scanner scanner = getFile("mapa.txt");

        int nCiudades = toInt(scanner.nextLine());
        pais.setCiudades(nCiudades);
        for(int i = 0; i < nCiudades; i++){
            pais.addNode(i);
        }

        int nCaminos = toInt(scanner.nextLine());
        for(int i = 0; i < nCaminos; i++){
            String[] data = scanner.nextLine().split(" ");
            int id1 = toInt(data[0]);
            int id2 = toInt(data[1]);
            int weight = toInt(data[2]);

            pais.addEdge(id1, id2, weight);
        }
        //System.out.println("'mapa.txt' leido");

        // Lectura de las edificaciones
        //System.out.println("Leyendo 'edificaciones.txt'");
        scanner = getFile("edificaciones.txt");
        for (int i = 0; i < nCiudades; i++){
              String[] data = scanner.nextLine().split(" ");
              //System.out.println("Ciudad|Casas|Edificios: " + Arrays.toString(data));
              int id_ciudad = toInt(data[0]);
              int nCasas = toInt(data[1]);
              int nEdificios = toInt(data[2]);

              Ciudad ciudad = pais.getNode(id_ciudad);

              // Leyendo las casas
              ciudad.setnCasas(nCasas);
              if(nCasas != 0){
                  data = scanner.nextLine().split(" ");
                  //System.out.println("Casas: " + Arrays.toString(data));
                  for (int j = 0; j < nCasas; j++){
                      ciudad.setCasa(j, new Casa(toInt(data[j])));
                  }
              }

              //Leyendo los edificios
              ciudad.setnEdificios(nEdificios);
              if(nEdificios != 0){
                  data = scanner.nextLine().split(" ");
                  //System.out.println("Edificios: " + Arrays.toString(data) + "\n");
                  for (int j = 0; j < nEdificios; j++){
                      ciudad.setEdificio(j, new Edificio(toInt(data[j])));
                  }
              }
        }
        //System.out.println("'edificaciones.txt' leido");

        // Lectura de la empresa
        //System.out.println("Leyendo 'empresa.txt'");
        scanner = getFile("empresa.txt");
        int precio_balon = toInt(scanner.nextLine());
        int precio_litro = toInt(scanner.nextLine());
        int precio_transporte = toInt(scanner.nextLine());

        pais.setEmpresa(new Empresa(precio_balon, precio_litro, precio_transporte));
        //System.out.println("'empresa.txt' leido");
    }

    /** (getFile)
    (String) (name)
    -------------------------
    Método para manejar errores al intentar leer un archivo
    -------------------------
    */
    private static Scanner getFile(String name){
        try{
            return new Scanner(new File(name));
        }catch(FileNotFoundException e){
            System.out.println("Archivo '" + name + "' no encontrado");
            e.printStackTrace();
            return null;
        }
    }

    /** (toInt)
    (String) (s)
    -------------------------
    Método auxiliar para transformar un string a un entero
    -------------------------
    */
    private static int toInt(String s){
        return Integer.parseInt(s);
    }
}
