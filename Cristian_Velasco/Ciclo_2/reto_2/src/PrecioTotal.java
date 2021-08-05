public class PrecioTotal {
    // Attributes

    private Double totalDispositivos = 0.0;
    private double totalPortatiles = 0.0;
    private Double totalTablets = 0.0;
    private Dispositivo listaDispositivos[];

    // Construtors

    public PrecioTotal(Dispositivo pDispositivos[]) {
        this.listaDispositivos = pDispositivos;
    }

    // Methods
    public void mostrarTotales() {

        for (Dispositivo el : listaDispositivos) {
            // System.out.println("elemento: " + el.calcularPrecio());
            if (el instanceof Dispositivo) {
                totalDispositivos += el.calcularPrecio();
            }

            if (el instanceof Tablet) {
                totalTablets += el.calcularPrecio();
            }

            if (el instanceof Portatil) {
                totalPortatiles += el.calcularPrecio();
            }
        }

        System.out.println("Total acerca de precios de dispositivos " + totalDispositivos);
        System.out.println("Total acerca de precios de tabletas " + totalTablets);
        System.out.println("Total acerca de precios de computadores portátiles " + totalPortatiles);
    }
}
