public class Dispositivo {
    // Attributes
    protected static final char CONSUMO_W = 'F';
    protected static final Double PRECIO_BASE = 200.0;
    protected static final Integer PESO_BASE = 2;

    protected Integer peso;
    protected char consumoW;
    protected Double precioBase;

    public Dispositivo() {
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W);
    }

    public Dispositivo(Double precioBase, Integer peso) {
        // codigo
        this(precioBase, peso, CONSUMO_W);
    }

    public Dispositivo(Double precioBase, Integer peso, char consumoW) {
        // codigo
        this.precioBase = precioBase;
        this.peso = peso;
        comprobarConsumoW(consumoW);
    }

    // Methods

    public void comprobarConsumoW(char consumoW) {

        if (consumoW > 2 && consumoW <= 20) {
            this.consumoW = consumoW;
        } else {
            this.consumoW = CONSUMO_W;
        }

    }

    public Double calcularPrecio() {

        Double adicion = 0.0;

        switch (consumoW) {
            case 'A':
                adicion += 80.0;
                break;
            case 'B':
                adicion += 70.0;
                break;
            case 'C':
                adicion += 60.0;
                break;
            case 'D':
                adicion += 50.0;
                break;
            case 'E':
                adicion += 40.0;
                break;
            case 'F':
                adicion += 30.0;
                break;
            default:
                break;
        }

        if (peso > 1 && peso <= 2) {
            adicion += 20.0;
        } else if (peso > 2 && peso <= 3) {
            adicion += 35.0;
        } else if (peso > 3 && peso <= 4) {
            adicion += 45.0;
        } else if (peso > 4) {
            adicion += 73.0;
        }

        return precioBase + adicion;
    }

    public static Double getPrecioBase() {
        return PRECIO_BASE;
    }

    public static char getConsumoW() {
        return CONSUMO_W;
    }

    public Integer getPeso() {
        return peso;
    }

}
