public class Dispositivo {
    // Attributes
    private static final int PESO_BASE = 2;
    private static final char CONSUMO_W_BASE = 'F';
    private static final double PRECIO_BASE = 200.0;

    private int peso;
    private char consumoW;
    private double precioBase;

    public Dispositivo() {
        super();
    }

    public Dispositivo(Double precioBase, Integer peso) {
        // codigo
    }

    public Dispositivo(Double precioBase, Integer peso, char consumoW) {
        // codigo
        comprobarconsumoW(consumoW);
    }

    // Methods

    public void comprobarConsumoW(char consumoW) {

        // if(//condition){
        // this.consumoW = consumoW;
        // } else {
        // this.consumoW = CONSUMO_W_BASE;
        // }

    }

    public Double calcularPrecio() {
        // codigo
        return precioBase + adicion;

    }

}
