public class NuevoProyecto {

    // Attributes
    private double monto;
    private double interes;
    private int periodo;

    // Methods
    public NuevoProyecto() {
        this.periodo = 0;
        this.monto = 0;
        this.interes = 0;
    }

    public NuevoProyecto(int pPeriodo, double pMonto, double pInteres) {
        this.periodo = pPeriodo;
        this.monto = pMonto;
        this.interes = pInteres;
    }

    public double calcularInteresSimple() {
        double interesSimple = this.monto * (this.interes / 100) * this.periodo;
        return Math.round(interesSimple);
    }

    public double calcularInteresCompuesto() {
        double interesCompuesto = this.monto * (Math.pow(1 + (this.interes / 100), this.periodo) - 1);
        return Math.round(interesCompuesto);
    }

    public double compararInversion(int pPeriodo, double pMonto, double pInteres) {
        periodo = pPeriodo;
        monto = pMonto;
        interes = pInteres;

        double diferencia = 0;

        double interesSimple = calcularInteresSimple();
        double interesCompuesto = calcularInteresCompuesto();
        diferencia = interesCompuesto - interesSimple;

        return diferencia;
    }

    public double compararInversion() {
        double diferencia = 0;

        diferencia = calcularInteresCompuesto() - calcularInteresSimple();

        return diferencia;
    }
}
