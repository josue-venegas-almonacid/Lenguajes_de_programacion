public class Empresa {
    private int PrecioBalon;
    private int PrecioLitro;
    private int PrecioTransporte;

    /** (Empresa)
    (int) (precioBalon)
    (int) (precioLitro)
    (int) (precioTransporte)
    -------------------------
    Constructor de la clase Empresa. Se registran los precios segun sus datos
    correspondientes
    -------------------------
    */
    public Empresa(int PrecioBalon, int PrecioLitro, int PrecioTransporte){
        this.PrecioBalon = PrecioBalon;
        this.PrecioLitro = PrecioLitro;
        this.PrecioTransporte = PrecioTransporte;
    }

    /** (getPrecioBalon)
    -------------------------
    Método que retorna el precio del balon de gas
    -------------------------
    */
    public int getPrecioBalon() {return this.PrecioBalon;}

    /** (getPrecioLitro)
    -------------------------
    Método que retorna el precio del litro de gas
    -------------------------
    */
    public int getPrecioLitro() {return this.PrecioLitro;}

    /** (getPrecioTransporte)
    -------------------------
    Método que retorna el costo por km de transporte
    -------------------------
    */
    public int getPrecioTransporte() {return this.PrecioTransporte;}
}
