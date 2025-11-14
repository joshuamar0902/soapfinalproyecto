
package com.example.demo.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.persistence.JoinColumn;
import java.time.LocalDateTime;



@Entity
@Table(name = "Actividad_Fisica")
public class ActividadFisicaModel { // Renombrado para seguir convenciones (opcional pero recomendado)
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_actividad")
    private Long idActividad;

    @ManyToOne
    @JoinColumn(name="id_usuario", nullable = false)
    private UsuarioModel usuario;

    @ManyToOne
    @JoinColumn(name="id_dispositivo") // nullable = false es el default para @ManyToOne, pero se puede dejar por claridad
    private DispositivosModel dispositivo; // Renombrado para seguir convenciones (asumiendo que la otra clase se llama DispositivoModel)

    @Column(name="fecha_hora_inicio", nullable = false)
    private LocalDateTime fechaHoraInicio;

    @Column(name="fecha_hora_fin", nullable = false)
    private LocalDateTime fechaHoraFin;

    @Column(name="km_recorridos")
    private Double kmRecorridos;

    @Column(name="calorias_quemadas")
    private Double caloriasQuemadas;

    @Column(name="frecuencia_cardiaca")
    private Integer frecuenciaCardiaca;

    @Column(name="oxigenacion")
    private Integer oxigenacion;


    // Getters y Setters actualizados a camelCase
    public Long getIdActividad() {
        return idActividad;
    }

    public void setIdActividad(Long idActividad) {
        this.idActividad = idActividad;
    }

    public UsuarioModel getUsuario() {
        return usuario;
    }

    public void setUsuario(UsuarioModel usuario) { // Asumiendo que UsuarioModel es el nombre correcto
        this.usuario = usuario;
    }

    public DispositivosModel getDispositivo() {
        return dispositivo;
    }

    public void setDispositivosModel(DispositivosModel dispositivo) {
        this.dispositivo = dispositivo;
    }
    public LocalDateTime getFechaHoraInicio() {
        return fechaHoraInicio;
    }

    public void setFechaHoraInicio(LocalDateTime fechaHoraInicio) {
        this.fechaHoraInicio = fechaHoraInicio;
    }
    public LocalDateTime getFechaHoraFin() {
        return fechaHoraFin;
    }
    public void setFechaHoraFin(LocalDateTime fechaHoraFin) {
        this.fechaHoraFin = fechaHoraFin;
    }
    public Double getKmRecorridos() {
        return kmRecorridos;
    }
    public void setKmRecorridos(Double kmRecorridos) {
        this.kmRecorridos = kmRecorridos;
    }
    public Double getCaloriasQuemadas() {
        return caloriasQuemadas;
    }
    public void setCaloriasQuemadas(Double caloriasQuemadas) {
        this.caloriasQuemadas = caloriasQuemadas;
    }
    public Integer getFrecuenciaCardiaca() {
        return frecuenciaCardiaca;
    }
    public void setFrecuenciaCardiaca(Integer frecuenciaCardiaca) {
        this.frecuenciaCardiaca = frecuenciaCardiaca;
    }
    public Integer getOxigenacion() {
        return oxigenacion;
    }
    public void setOxigenacion(Integer oxigenacion) {
        this.oxigenacion = oxigenacion;
    }
}
