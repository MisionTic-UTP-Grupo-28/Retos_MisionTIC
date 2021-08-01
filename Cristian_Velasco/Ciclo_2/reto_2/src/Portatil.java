public class Portatil extends Dispositivo {
    // Constantes y atributos

    private static final Integer DISCO_DURO_BASE = 250;

    private Integer discoDuro;

    // Constructor
    public Portatil() {
        // codigo
    }

    public Portatil(Double precioBase, Integer peso) {
        // codigo
    }

    public Portatil(Double precioBase, Integer peso, char consumoW, Integer discoDuro) {
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
