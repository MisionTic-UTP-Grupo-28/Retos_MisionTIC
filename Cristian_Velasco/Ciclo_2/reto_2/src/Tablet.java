public class Tablet extends Dispositivo {
    // Attributes and Constants

    private static final Integer MEMORIA_RAM_BASE = 1;

    private Integer memoriaRam;

    // Constructor

    public Tablet() {
        super();
    }

    public Tablet(Double precioBase, Integer peso) {
    }

    public Tablet(Double precioBase, Integer peso, char consumoW, Integer memoriaRam) {
        // codigo
    }

    // Métodos
    public Double calcularPrecio() {
        // codigo
        Double precioFinal = 0.0;
        Integer valorConsumoW = 0;

        precioFinal = super.calcularPrecio() + valorConsumoW;

        return precioFinal;
    }
}
