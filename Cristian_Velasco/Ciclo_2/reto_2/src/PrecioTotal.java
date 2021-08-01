public class PrecioTotal {
    // Attributes

    private Double totalDispositivos;
    private double totalPortatiles;
    private Double totalTablets;
    private Dispositivo listaDispositivos[];

    // Construtors
    public PrecioTotal() {
        this.totalDispositivos = 0.0;
        this.totalPortatiles = 0.0;
        this.totalTablets = 0.0;
    }

    public PrecioTotal(Dispositivo pDispositivos[]) {
        this.totalDispositivos = 0.0;
        this.totalPortatiles = 0.0;
        this.totalTablets = 0.0;

        this.listaDispositivos = pDispositivos;

    }

    // Methods
    public void mostrarTotales() {

        for (Dispositivo el : listaDispositivos) {
            if (el instanceof Dispositivo) {
                totalDispositivos += el.calcularPrecio();
            } else if (el instanceof Tablet) {
                totalTablets += el.calcularPrecio();
            } else if (el instanceof Portatil) {
                totalPortatiles += el.calcularPrecio();
            }
        }

        System.out.println("Total acerca de precios de dispositivos " + totalDispositivos);
        System.out.println("Total acerca de precios de tabletas " + totalTablets);
        System.out.println("Total acerca de precios de computadores portátiles " + totalPortatiles);
    }
}
