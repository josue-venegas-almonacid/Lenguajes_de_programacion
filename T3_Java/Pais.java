import java.util.ArrayList;


interface Grafo{
      int nEdges = 0;
      int nNodes = 0;

      int edgeWeight(int id1, int id2);
      int[] shortestPath(int id1, int id2);
      int addEdge(int id1, int id2, int weight);
      void addNode(int id);
      Ciudad getNode(int id);
}

class Pais implements Grafo{
    private Empresa empresa;
    private Ciudad[] ciudades;

    /** (setCiudades)
    (int) (nCiudades)
    -------------------------
    Método para registrar las ciudades en un arreglo de nCiudades
    -------------------------
    */
    public void setCiudades(int nCiudades){
        ciudades = new Ciudad[nCiudades];
    }

    /** (getCiudades)
    -------------------------
    Método que retorna las ciudades del pais
    -------------------------
    */
    public Ciudad[] getCiudades(){
        return this.ciudades;
    }

    /** (getEmpresa)
    -------------------------
    Método que retorna la empresa que pertenece al pais
    -------------------------
    */
    public Empresa getEmpresa(){
        return this.empresa;
    }

    /** (setEmpresa)
    (Empresa) (empresa)
    -------------------------
    Método para registrar la empresa
    -------------------------
    */
    public void setEmpresa(Empresa empresa){
        this.empresa = empresa;
    }

    @Override
    public int edgeWeight(int id1, int id2){
        return getNode(id1).getConnection(id2);
    }
    @Override
    public int[] shortestPath(int id1, int id2){
        return new int[] {0};
    }
    @Override
    public int addEdge(int id1, int id2, int weight){
        getNode(id1).addConnection(id2, weight);
        getNode(id2).addConnection(id1, weight);
        return weight;
    }
    @Override
    public void addNode(int id){
        ciudades[id] = new Ciudad(this, id);
    }

    /** (getNode)
    (int) (id)
    -------------------------
    Método que retorna la ciudad segun el id asociado
    -------------------------
    */
    @Override
    public Ciudad getNode(int id){
        return ciudades[id];
    }
}
