public class Tablet extends Dispositivo {
    // Attributes and Constants

    private static final Integer MEMORIA_RAM_BASE = 1;

    private Integer memoriaRam;

    // Constructor

    public Tablet() {
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W, MEMORIA_RAM_BASE);
    }

    public Tablet(Double precioBase, Integer peso) {
        this(precioBase, peso, CONSUMO_W, MEMORIA_RAM_BASE);
    }

    public Tablet(Double precioBase, Integer peso, char consumoW, Integer memoriaRam) {
        // codigo
        super(precioBase, peso, consumoW);
        this.memoriaRam = memoriaRam;
    }

    // Métodos
    public Double calcularPrecio() {
        // codigo
        Double adicion = super.calcularPrecio();

        if (memoriaRam > 1 && memoriaRam <= 2) {
            adicion += 18;
        }
        if (memoriaRam > 2 && memoriaRam <= 4) {
            adicion += 37;
        }
        if (memoriaRam > 4) {
            adicion += 69;
        }

        return adicion;
    }

    public Integer getMemoriaRam() {
        return memoriaRam;
    }
}
