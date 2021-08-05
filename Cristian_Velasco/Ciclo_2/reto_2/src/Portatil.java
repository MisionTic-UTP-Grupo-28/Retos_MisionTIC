public class Portatil extends Dispositivo {
    // Constantes y atributos

    private static final Integer DISCO_DURO_BASE = 250;

    private Integer discoDuro;

    // Constructor
    public Portatil() {
        // codigo
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W, DISCO_DURO_BASE);
    }

    public Portatil(Double precioBase, Integer peso) {
        this(precioBase, peso, CONSUMO_W, DISCO_DURO_BASE);
        // codigo
    }

    public Portatil(Double precioBase, Integer peso, char consumoW, Integer discoDuro) {
        // codigo
        super(precioBase, peso, consumoW);
        this.discoDuro = discoDuro;
    }

    // Métodos
    public Double calcularPrecio() {
        // codigo
        Double adicion = super.calcularPrecio();

        if (discoDuro > 250 && discoDuro <= 500) {
            adicion += 25;
        }
        if (discoDuro > 500 && discoDuro <= 1000) {
            adicion += 65;
        }
        if (discoDuro > 1000) {
            adicion += 89;
        }

        return adicion;
    }
}
