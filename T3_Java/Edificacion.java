public abstract class Edificacion{
      private int Consumo;

      /** (Edificacion)
      (int) (consumo)
      -------------------------
      Constructor de la clase Edificacion
      -------------------------
      */
      public Edificacion(int consumo){
            this.Consumo = consumo;
      }

      /** (getConsumo)
      -------------------------
      Metodo que retorna el consumo de la edificacion
      -------------------------
      */
      public int getConsumo(){return this.Consumo;}

      /** (setConsumo)
      (int) (consumo)
      -------------------------
      Método para registrar el consumo de una edificacion
      -------------------------
      */
      public void setConsumo(int consumo){this.Consumo = consumo;}

}
