/** Atributos agregados:
(HashMap<Integer, Integer>) connections: Guardamos las conexiones de cada ciudad en un
diccionario, donde el primer valor corresponde al id de la ciudad con la que tiene un arco
y el segundo valor corresponde a la distancia entre ellas (peso)
*/

import java.util.HashMap;
import java.util.ArrayList;


public class Ciudad{
      private int id;
      private int nEdificios;
      private int nCasas;
      private HashMap<Integer, Integer> connections;
      private Pais pais;

      private Edificio[] edificios;
      private Casa[] casas;

      /** (Ciudad)
      (Pais) (pais)
      (int) (id)
      -------------------------
      Constructor de la clase Ciudad, con el pais y el id correspondiente.
      Se crea un diccionario con las ciudades con las que tiene conexion
      -------------------------
      */
      public Ciudad(Pais pais, int id){
          this.pais = pais;
          this.id = id;
          this.connections = new HashMap<Integer, Integer>();
      }

      /** (addConnection)
      (int) (id)
      (int) (weight)
      -------------------------
      Método que agrega una ciudad id al diccionario actual de conexiones y la
      distancia entre ellas
      -------------------------
      */
      public void addConnection(int id, int weight){
          this.connections.put(id, weight);
      }

      /** (getConnection)
      (int) (id)
      -------------------------
      Método que retorna la distancia de la ciudad id con la actual ciudad
      -------------------------
      */
      public int getConnection(int id){
          return this.connections.get(id);
      }

      /** (getConnections)
      -------------------------
      Método que retorna el diccionario con la menor distancia que tiene la ciudad actual con las demas ciudades
      -------------------------
      */
      public HashMap<Integer, Integer> getConnections(){
          HashMap<Integer, Integer> connections = new HashMap<Integer, Integer>(this.connections);
          for (int key : this.connections.keySet()) {
              HashMap<Integer, Integer> newConnections = pais.getNode(key).getNeighbours();
              for(int newKey : newConnections.keySet()){
                  if(newKey != this.id){
                      if(connections.containsKey(newKey)){
                        if(newConnections.get(newKey) + connections.get(key) < connections.get(newKey)){
                            connections.replace(newKey, newConnections.get(newKey) + connections.get(key));
                        }
                      } else    {
                          connections.put(newKey, newConnections.get(newKey));
                      }
                }
              }
          }
          return connections;
      }

      /** (getNeighbours)
      -------------------------
      Método que retorna un diccionario con las ciudades vecinas a la ciudad actual
      -------------------------
      */
      public HashMap<Integer, Integer> getNeighbours(){
          return this.connections;
      }

      /** (getId)
      (int) (id)
      -------------------------
      Método que retorna el id de la ciudad actual
      -------------------------
      */
      public int getId() {return id;}

      /** (setnEdificios)
      (int) (n)
      -------------------------
      Método que registra la cantidad de edificios leida de una ciudad
      -------------------------
      */
      public void setnEdificios(int n){
          this.nEdificios = n;
          this.edificios = new Edificio[this.nEdificios];
      }

      /** (getnEdificios)
      -------------------------
      Método que retorna la cantidad de edificios leida de una ciudad
      -------------------------
      */
      public int getnEdificios() {
          return this.nEdificios;
      }

      /** (getEdificios)
      -------------------------
      Método que retorna el arreglo de edificios de una ciudad
      -------------------------
      */
      public Edificio[] getEdificios(){
          return this.edificios;
      }

      /** (getConsumoEdificios)
      -------------------------
      Método que retorna el consumo total de todos los edificios de la ciudad
      -------------------------
      */
      public int getConsumoEdificios(){
          int sum = 0;
          for(int i = 0; i < this.nEdificios; i++){
              sum += edificios[i].getConsumo();
          }
          return sum;
      }

      /** (setEdificio)
      (int) (id)
      (Edificio) (edificio)
      -------------------------
      Método que asocia un id con un edificio
      -------------------------
      */
      public void setEdificio(int id, Edificio edificio){
          this.edificios[id] = edificio;
      }

      /** (setnCasas)
      (int) (n)
      -------------------------
      Método que registra la cantidad de casas leida de una ciudad
      -------------------------
      */
      public void setnCasas(int n){
          this.nCasas = n;
          this.casas = new Casa[this.nCasas];
      }

      /** (getnCasa)
      -------------------------
      Método que retorna la cantidad de edificios leida de una ciudad
      -------------------------
      */
      public int getnCasa() {
          return this.nCasas;
      }

      /** (getCasas)
      -------------------------
      Método que retorna el arreglo de casas de una ciudad
      -------------------------
      */
      public Casa[] getCasas(){
          return this.casas;
      }

      /** (getConsumoCasas)
      -------------------------
      Método que retorna el consumo total de todas las casas de la ciudad
      -------------------------
      */
      public int getConsumoCasas(){
          int sum = 0;
          for(int i = 0; i < this.nCasas; i++){
              sum += casas[i].getConsumo();
          }
          return sum;
      }

      /** (setCasa)
      (int) (id)
      (Casa) (casa)
      -------------------------
      Método que asocia un id con un casa
      -------------------------
      */
      public void setCasa(int id, Casa casa){
          this.casas[id] = casa;
      }
      
}
