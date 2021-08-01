public class Dispositivo {
    // Attributes
    private static final Integer PESO_BASE = 2;
    private static final char CONSUMO_W_BASE = 'F';
    private static final Double PRECIO_BASE = 200.0;

    private Integer peso;
    private char consumoW;
    private Double precioBase;

    public Dispositivo() {
        super();
    }

    public Dispositivo(Double precioBase, Integer peso) {
        // codigo
    }

    public Dispositivo(Double precioBase, Integer peso, char consumoW) {
        // codigo
        comprobarConsumoW(consumoW);
    }

    // Methods

    public void comprobarConsumoW(char consumoW) {

        if (consumoW == 'F') {
            this.consumoW = consumoW;
        } else {
            this.consumoW = CONSUMO_W_BASE;
        }

    }

    public Double calcularPrecio() {

        Double precioFinal = 0.0;
        Integer valorPorConsumoW = 0;
        Integer valorPorPeso = 0;

        switch (consumoW) {
            case 'A':
                valorPorConsumoW = 80;
                break;
            case 'B':
                valorPorConsumoW = 70;
                break;
            case 'C':
                valorPorConsumoW = 60;
                break;
            case 'D':
                valorPorConsumoW = 50;
                break;
            case 'E':
                valorPorConsumoW = 40;
                break;
            case 'F':
                valorPorConsumoW = 30;
                break;
            default:
                break;
        }

        if (peso > 1 && peso <= 2) {
            valorPorPeso += 20;
        } else if (peso > 2 && peso <= 3) {
            valorPorPeso += 35;
        } else if (peso > 3 && peso <= 4) {
            valorPorPeso += 45;
        } else if (peso > 4) {
            valorPorPeso += 73;
        }

        precioFinal = precioBase + valorPorConsumoW + valorPorPeso;

        return precioFinal;

    }

}
